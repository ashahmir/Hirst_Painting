# 🎨 Turtle Dot Grid Generator (Inspired by Hirst Painting)

This Python script uses the built-in `turtle` module to generate a beautiful **10x10 dot grid** with randomly selected colors. It's inspired by the artistic style of **Damien Hirst** and leverages RGB values to create a soft, pastel-colored aesthetic.

## 🐍 Built With

- Python 3.x
- `turtle` graphics module
- `random` for color selection

## 📸 Preview

The turtle draws 100 colorful dots arranged in a 10x10 grid. Each dot is randomly assigned a soft color from a pre-selected palette.

The color palette was selected using cologram.py and one of the origin Hirst Paintings.

## 🎯 Features

- Uses RGB color tuples (not just named colors)
- Clean grid layout (10 rows × 10 columns)
- Turtle trail is hidden for smooth visuals
- Easily customizable colors and spacing

## 🧠 How It Works

- The turtle starts at the bottom-left of the screen.
- It moves horizontally, drawing a dot every 50 pixels.
- After 10 dots, it moves up vertically and resets to the starting X position.
- This process is repeated for 10 rows.

🎨 Customize
Change rgb_colors to your own palette.

Adjust dot size via dot(20, ...).

Modify grid size or spacing by changing range(10) and forward(50).

📄 License
This project is open-source and free to use for learning or creative purposes.

Happy coding and painting with Python Turtle! 🐢✨


Let me know if you want to add a GIF of the turtle drawing it in real-time or tweak the wording for your personal GitHub profile.
