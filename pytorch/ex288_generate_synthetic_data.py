import random
import string
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import platform

# ============================================================================
# CONFIGURATION
# ============================================================================
OUTPUT_DIR = "."
NUM_IMAGES_TRUE = 500   # Images with letters
NUM_IMAGES_FALSE = 500  # Images without letters

# Image settings
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
BACKGROUND_COLOR = (255, 255, 255)  # White background

# Text settings
MIN_LETTERS = 3
MAX_LETTERS = 10
FONT_SIZE_MIN = 20
FONT_SIZE_MAX = 60
MIN_LETTERS_PER_IMAGE = 1
MAX_LETTERS_PER_IMAGE = 8

# ============================================================================
# MACOS FONT DETECTION
# ============================================================================

def get_macos_fonts():
    """Get available TrueType fonts on macOS ARM64."""
    fonts = []
    
    # macOS system font directories
    font_dirs = [
        os.path.expanduser("~/Library/Fonts"),
        "/Library/Fonts",
        "/System/Library/Fonts",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    
    # Common macOS fonts
    macos_fonts = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Times New Roman.ttf",
        "/System/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Courier New.ttf",
        "/Library/Fonts/Arial.ttf",
        "/Library/Fonts/Helvetica.ttf",
        "/Library/Fonts/Times New Roman.ttf",
        "/System/Library/Fonts/San Francisco.ttf",
    ]
    
    # Check user and system fonts
    for font_dir in font_dirs:
        if os.path.isdir(font_dir):
            try:
                for filename in os.listdir(font_dir):
                    if filename.endswith(('.ttf', '.otf', '.ttc')):
                        full_path = os.path.join(font_dir, filename)
                        fonts.append(full_path)
            except PermissionError:
                pass
    
    # Check specific macOS fonts
    for font_path in macos_fonts:
        if os.path.exists(font_path):
            fonts.append(font_path)
    
    # Remove duplicates
    fonts = list(set(fonts))
    
    return fonts


def get_available_fonts():
    """Get a list of available system fonts (macOS optimized)."""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        return get_macos_fonts()
    
    # Fallback for other systems
    fonts = []
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/Windows/Fonts/arial.ttf",
        "/System/Library/Fonts/Arial.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
    ]
    
    for path in font_paths:
        if os.path.exists(path):
            fonts.append(path)
    
    return fonts


def get_default_macos_font(font_size):
    """Get default macOS font if no TrueType fonts available."""
    try:
        # Try to use system font
        font_path = "/System/Library/Fonts/Helvetica.ttc"
        if os.path.exists(font_path):
            return ImageFont.truetype(font_path, font_size)
    except Exception:
        pass
    
    # Fallback to default
    return ImageFont.load_default()


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_random_font(available_fonts, font_size):
    """Get a random font from available fonts."""
    if available_fonts:
        font_path = random.choice(available_fonts)
        try:
            return ImageFont.truetype(font_path, font_size)
        except Exception as e:
            # If font loading fails, try default macOS font
            try:
                return get_default_macos_font(font_size)
            except Exception:
                pass
    
    # Fallback to default font
    return ImageFont.load_default()


def generate_random_letters(min_letters=MIN_LETTERS, max_letters=MAX_LETTERS):
    """Generate a random string of letters (a-zA-Z)."""
    num_letters = random.randint(min_letters, max_letters)
    return ''.join(random.choice(string.ascii_letters) for _ in range(num_letters))


def get_random_color():
    """Get a random non-white color for text."""
    # Avoid very light colors (too close to white background)
    return (
        random.randint(0, 200),
        random.randint(0, 200),
        random.randint(0, 200)
    )


def get_text_bbox(draw, text, font):
    """Get text bounding box (compatible with PIL versions)."""
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]  # width, height
    except Exception:
        # Fallback for older PIL versions
        return draw.textsize(text, font=font)


# ============================================================================
# IMAGE GENERATION FUNCTIONS
# ============================================================================

def generate_image_with_letters(available_fonts):
    """Generate an image with random English letters."""
    # Create blank image
    image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)
    
    # Randomly decide number of text elements to add
    num_text_elements = random.randint(MIN_LETTERS_PER_IMAGE, MAX_LETTERS_PER_IMAGE)
    
    for _ in range(num_text_elements):
        # Generate random text
        text = generate_random_letters()
        
        # Random font size
        font_size = random.randint(FONT_SIZE_MIN, FONT_SIZE_MAX)
        font = get_random_font(available_fonts, font_size)
        
        # Get text dimensions
        try:
            text_width, text_height = get_text_bbox(draw, text, font)
        except Exception:
            text_width = font_size * len(text) // 2
            text_height = font_size
        
        # Random position (ensure text stays within bounds)
        x = random.randint(5, max(5, IMAGE_WIDTH - text_width - 5))
        y = random.randint(5, max(5, IMAGE_HEIGHT - text_height - 5))
        
        # Random color (not white)
        color = get_random_color()
        
        # Optional: Add rotation effect
        if random.random() > 0.7:  # 30% chance of rotation
            angle = random.randint(-30, 30)
            try:
                # Create text image and rotate
                text_img = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT), (255, 255, 255, 0))
                text_draw = ImageDraw.Draw(text_img)
                text_draw.text((x, y), text, font=font, fill=(*color, 255))
                text_img = text_img.rotate(angle, expand=False, resample=Image.Resampling.BICUBIC)
                image = Image.alpha_composite(image.convert('RGBA'), text_img).convert('RGB')
            except Exception:
                # Fallback to non-rotated text
                draw.text((x, y), text, font=font, fill=color)
        else:
            draw.text((x, y), text, font=font, fill=color)
    
    # Optional: Add some noise for realism
    if random.random() > 0.8:  # 20% chance of noise
        image = add_noise(image, noise_level=0.05)
    
    return image


def generate_image_without_letters():
    """Generate a blank image without any letters."""
    image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), BACKGROUND_COLOR)
    
    # Optional: Add some subtle noise or patterns to vary the images
    if random.random() > 0.6:  # 40% chance of background variation
        image = add_subtle_background_variation(image)
    
    return image


def add_noise(image, noise_level=0.05):
    """Add random noise to an image."""
    try:
        img_array = np.array(image)
        noise = np.random.normal(0, 255 * noise_level, img_array.shape)
        noisy_array = np.clip(img_array + noise, 0, 255).astype(np.uint8)
        return Image.fromarray(noisy_array)
    except Exception as e:
        print(f"Warning: Could not add noise: {e}")
        return image


def add_subtle_background_variation(image):
    """Add subtle color variation to the background."""
    try:
        img_array = np.array(image)
        
        # Create a subtle gradient or color variation
        variation = np.random.randint(-10, 10, img_array.shape)
        varied_array = np.clip(img_array + variation, 0, 255).astype(np.uint8)
        
        return Image.fromarray(varied_array)
    except Exception as e:
        print(f"Warning: Could not add background variation: {e}")
        return image


# ============================================================================
# MAIN GENERATOR FUNCTION
# ============================================================================

def generate_synthetic_dataset(output_dir=OUTPUT_DIR,
                               num_true=NUM_IMAGES_TRUE,
                               num_false=NUM_IMAGES_FALSE,
                               verbose=True):
    """Generate synthetic dataset of PNG images with and without letters."""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get available fonts
    available_fonts = get_available_fonts()
    if not available_fonts:
        if verbose:
            print("⚠️  Warning: No TrueType fonts found. Using default font.")
            print("   Install fonts to /Library/Fonts for better variety.\n")
    else:
        if verbose:
            print(f"✓ Found {len(available_fonts)} available font(s)")
    
    if verbose:
        print(f"\nGenerating {num_true} images with letters...")
        print(f"Generating {num_false} images without letters...")
        print(f"Output directory: {output_dir}\n")
    
    image_counter = 0
    
    # Generate images with letters (true)
    for i in range(num_true):
        try:
            image = generate_image_with_letters(available_fonts)
            filename = f"{image_counter}-true.png"
            filepath = os.path.join(output_dir, filename)
            image.save(filepath, 'PNG')
            image_counter += 1
            
            if verbose and (i + 1) % 50 == 0:
                print(f"  ✓ Generated {i + 1}/{num_true} images with letters")
        except Exception as e:
            print(f"  ✗ Error generating image {i}: {e}")
            continue
    
    if verbose:
        print(f"  ✓ Completed all {num_true} images with letters\n")
    
    # Generate images without letters (false)
    for i in range(num_false):
        try:
            image = generate_image_without_letters()
            filename = f"{image_counter}-false.png"
            filepath = os.path.join(output_dir, filename)
            image.save(filepath, 'PNG')
            image_counter += 1
            
            if verbose and (i + 1) % 50 == 0:
                print(f"  ✓ Generated {i + 1}/{num_false} images without letters")
        except Exception as e:
            print(f"  ✗ Error generating image {i}: {e}")
            continue
    
    if verbose:
        print(f"  ✓ Completed all {num_false} images without letters\n")
    
    # Verify and report
    all_files = [f for f in os.listdir(output_dir) if f.endswith('.png')]
    true_files = [f for f in all_files if '-true.png' in f]
    false_files = [f for f in all_files if '-false.png' in f]
    
    if verbose:
        print("="*70)
        print("GENERATION COMPLETE")
        print("="*70)
        print(f"Total images generated: {len(all_files)}")
        print(f"  - With letters (true): {len(true_files)}")
        print(f"  - Without letters (false): {len(false_files)}")
        print(f"Output location: {output_dir}")
        print(f"System: {platform.system()} ARM64")
        print("="*70)
    
    return len(all_files)


# ============================================================================
# PREVIEW FUNCTION
# ============================================================================

def generate_and_display_samples(num_samples=4):
    """Generate and save sample images for preview."""
    print("\nGenerating sample images for preview...\n")
    
    available_fonts = get_available_fonts()
    
    sample_dir = os.path.join(OUTPUT_DIR, "samples")
    os.makedirs(sample_dir, exist_ok=True)
    
    # Generate samples with letters
    for i in range(num_samples):
        image = generate_image_with_letters(available_fonts)
        filepath = os.path.join(sample_dir, f"sample_{i:02d}-true.png")
        image.save(filepath, 'PNG')
        print(f"  ✓ Saved {os.path.basename(filepath)}")
    
    # Generate samples without letters
    for i in range(num_samples):
        image = generate_image_without_letters()
        filepath = os.path.join(sample_dir, f"sample_{num_samples + i:02d}-false.png")
        image.save(filepath, 'PNG')
        print(f"  ✓ Saved {os.path.basename(filepath)}")
    
    print(f"\nSample images saved to {sample_dir}/")


# ============================================================================
# ADVANCED GENERATION OPTIONS
# ============================================================================

def generate_with_custom_settings(output_dir=OUTPUT_DIR,
                                  num_true=500,
                                  num_false=500,
                                  image_size=(224, 224),
                                  min_letters=1,
                                  max_letters=10,
                                  font_size_range=(20, 60)):
    """Generate synthetic dataset with custom settings."""
    
    global IMAGE_WIDTH, IMAGE_HEIGHT, MIN_LETTERS, MAX_LETTERS
    global FONT_SIZE_MIN, FONT_SIZE_MAX
    
    IMAGE_WIDTH, IMAGE_HEIGHT = image_size
    MIN_LETTERS, MAX_LETTERS = min_letters, max_letters
    FONT_SIZE_MIN, FONT_SIZE_MAX = font_size_range
    
    return generate_synthetic_dataset(output_dir, num_true, num_false)


# ============================================================================
# COMMAND LINE INTERFACE
# ============================================================================

if __name__ == "__main__":
    import sys
    
    print("="*70)
    print("SYNTHETIC DATA GENERATOR FOR CHARACTER DETECTION")
    print("macOS ARM64 Optimized")
    print("="*70)
    
    # Parse command line arguments
    num_true = int(sys.argv[1]) if len(sys.argv) > 1 else NUM_IMAGES_TRUE
    num_false = int(sys.argv[2]) if len(sys.argv) > 2 else NUM_IMAGES_FALSE
    generate_samples = "--samples" in sys.argv
    
    print(f"\nSystem Information:")
    print(f"  Platform: {platform.system()} {platform.machine()}")
    print(f"  Python: {platform.python_version()}\n")
    
    print(f"Configuration:")
    print(f"  Image size: {IMAGE_WIDTH}x{IMAGE_HEIGHT}")
    print(f"  Letters per image (with text): {MIN_LETTERS_PER_IMAGE}-{MAX_LETTERS_PER_IMAGE}")
    print(f"  Letters per text element: {MIN_LETTERS}-{MAX_LETTERS}")
    print(f"  Font size range: {FONT_SIZE_MIN}-{FONT_SIZE_MAX}")
    print(f"  Background color: RGB{BACKGROUND_COLOR}\n")
    
    # Generate dataset
    generate_synthetic_dataset(output_dir=OUTPUT_DIR,
                               num_true=num_true,
                               num_false=num_false)
    
    # Generate preview samples if requested
    if generate_samples:
        generate_and_display_samples(num_samples=5)
    
    print("\nTo use this generator in your code:")
    
