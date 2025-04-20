# 🦾 Phantom Hands – Gesture-Controlled Omnidirectional Car

A real-time hand-controlled robot that uses computer vision to drive a 4-wheeled omnidirectional vehicle via gesture recognition.

![Phantom Hands](./images/demo.jpg)

---

## 🤖 Overview

**Phantom Hands** is a robotics and computer vision project that interprets hand gestures using OpenCV and MediaPipe to control the movement of a custom-built car through Arduino. The robot moves forward, backward, and turns left or right based on dynamic hand poses detected in real time via webcam.

Built at **MakeUofT 2024** over a period of 24 hours, this project merges gesture-based interaction, embedded systems, and real-time motor control into a fun and intuitive robotic platform.

---

## 🛠️ Features

- Real-time hand tracking and gesture classification (OpenCV + MediaPipe)
- Directional mapping of gestures to motor control
- 4 independently controlled motors powered by dual L298N drivers
- Smooth USB serial communication between Python and Arduino
- Fully modular and extensible codebase (gesture logic and motor control decoupled)

---

## ✋ Gesture Mapping

| Gesture      | Action         |
|--------------|----------------|
| Hand Down    | Move Forward   |
| Hand Up      | Move Backward  |
| Hand Right   | Turn Right     |
| Hand Left    | Turn Left      |

---

## 🎥 Demo Video

[![Watch the Demo](./images/demo-thumbnail.jpg)](https://www.youtube.com/watch?v=your-demo-link)

> _Note: For demo purposes, the rear wheels were kept stationary while the front motors demonstrated gesture-controlled movement. The full codebase supports 4-wheel synchronized drive, and all motors were successfully tested._

---


