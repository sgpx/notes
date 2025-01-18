using Microsoft.AspNetCore.Mvc.RazorPages;

namespace GreetingApp.Pages
{
    public class GreetingModel : PageModel
    {
        public int Id { get; set; }

        // Name of the product
        public required string XName { get; set; }

        // Price of the product
        public decimal Price { get; set; }
        public void OnGet()
        {
            Console.WriteLine("exec 123");
            // This method is executed on GET requests
        }
    }
}