# 🔓 Pop the Lock: Face Controlled Edition 🎮

### Download: https://github.com/KuentsenDorji/Pop-The-Lock/releases/tag/v.1.0.0

A webcam based, gesture controlled arcade game built with Python and Pygame. Instead of tapping a keyboard or clicking a mouse, the player controls the game with real time face tracking using their webcam and the closing/opening of their mouth to collect points. 



[<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/b0b5e4d8-0f7a-4f13-987e-b3a2b1e2c826" />](https://s7.ezgif.com/tmp/ezgif-71762db1f6d70767.gif)



**The Goal:** The classic Pop the Lock mechanic, but driven by computer vision. Wait for the rotating indicator to hit the target, then **close your mouth** to score a point and reverse direction. Miss the target, and it's game over!

## ✨ Features
*   **Real Time Gesture Controls:** Face and mouth tracking powered by MediaPipe FaceMesh and cvzone.
*   **Threaded Performance:** Background threaded camera capture ensures gameplay rendering stays buttery smooth, entirely independent of webcam latency.
*   **Dynamic UI:** HSV based dynamic color theming that shifts as your score gets higher.
*   **Scene Management:** Clean multi screen flow transitioning from Welcome → Game → End.

## 🛠️ Tech Stack
*   **Python 3.9+**
*   **Pygame:** Rendering, UI, and main game loop.
*   **OpenCV (cv2):** Hardware webcam capture and image processing.
*   **MediaPipe / cvzone:** Machine learning pipeline for real time facial landmark detection.

## 🚀 Getting Started

### Prerequisites
*   Python 3.9 or newer installed on your machine.
*   A working webcam.

### Installation

1. Clone the repository:
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
```

```bash
pip install -r requirements.txt
```

```bash
python main.py
```

```text
project/
├── main.py              # Entry point and main game loop
├── config.py            # Global constants and color configs
├── utils.py             # Helper functions (math, conversions)
├── face_tracking.py     # Background thread for webcam/MediaPipe
├── welcome_window.py    # Start screen logic
├── game_window.py       # Core gameplay loop and drawing
├── end_window.py        # Game over screen and score display
├── assets/              
│   └── music/           # Sound effects and background tracks
└── requirements.txt
```

🧠 Technical Highlights & What I Learned
I ran into several distinct engineering challenges that forced me to step outside of basic tutorials and learn how to architect real systems:

1. Game State (Scene) Management
Initially, everything lived in one giant while loop, which quickly became impossible to manage. I learned how to modularize the application into distinct states (Welcome, Game, End). This taught me the importance of separation of concerns, each screen now handles its own event polling and rendering, making the code highly scalable and much easier to debug. Through this project I learned the importance of abstraction and encapsulation as well as how important good design is for scalability.

2. Trigonometry for UI Rendering
UI mapping isn't just about placing rectangles on a grid. To recreate the circular path of "Pop the Lock," I had to use geometry. I learned how to use sin and cos functions to continuously calculate the dynamic X and Y coordinates of the rotating player token, mapping its position perfectly around the radius of the central circle. I also used trigonometric wave functions for the loading screen.

3. Bridging C++ Libraries and Python (The Vision Pipeline)
Getting the webcam footage to display inside a Pygame window required understanding data formats. OpenCV processes hardware camera frames as raw Numpy arrays in BGR color space, but Pygame requires RGB Surface objects. I successfully built a real time pipeline to capture, convert the color space, transpose the arrays, and render them seamlessly without dropping frames.

4. Overcoming Webcam Bottlenecks via Threading
Originally, webcam capture and face mesh inference ran on the main thread. This meant Pygame had to wait on cap.read() and MediaPipe's inference before drawing the next frame, any camera hiccup stalled the whole UI. To fix this, I moved capture and detection into a dedicated background thread that continuously writes the latest frame and landmarks to shared state, protected by a threading.Lock(). The render loop now just reads whatever is latest. As a result, UI animations stay completely smooth at a consistent frame rate regardless of hardware latency.

5. Profiling Before Optimizing
Rather than assuming the machine learning inference was the slow part of the loop, I timed each pipeline stage separately (cap.read() vs. findFaceMesh()). That isolated the real bottleneck to cap.read() itself driven by webcam backend/format overhead (default YUY2 capture vs. MJPG), not the ML model. It was a great lesson in proving assumptions with data before trying to optimize code. After threading the camera logic, changing the webcam fromat overhead, and optimizing the camera resolution the fps went from around 10 to 30! The webcam also stopped stalling and booted as soon as the program started, causing around a 90 percent reduction in startup time (10s to 1s) and around a 3 times increase in runtime (10fps to 30fps).

Overall this was a very fun project to make that taught me alot about how to program efficently and how to cleanly combine multiple complex libraries and manage their dependencies for a smooth deployment!
