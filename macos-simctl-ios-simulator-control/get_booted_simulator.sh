xcrun simctl list | grep -i booted | head -n 1 | sed -r "s/.+\(([A-Z0-9-]+)\).+/\1/"
