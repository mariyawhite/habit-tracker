# Habit Tracker

## Overview

A CLI-based habit tracker that logs task sessions, including emotional state before and after completion.

Built to explore lightweight state management, structured logging, and user interaction patterns using local file storage.

---

## Features

- CLI workflow (`start` / `end`)  
- Tracks:
  - habit  
  - feeling before  
  - activity performed  
  - feeling after  
  - session duration  
- Per-habit CSV logging  
- Session persistence using a temporary `.current_session` file  
- Input validation for required fields  

---

## Usage

### Start a session
```bash
python3 habit.py start
```

### End a session
```bash
python3 habit.py end
```

## Design Notes

- Separates session lifecycle into start and end phases
- Uses file-based state to persist in-progress sessions
- Logs structured data for later analysis
- Designed to be simple, transparent, and easy to extend

## Context

This project was inspired by behavioral activation principles, exploring the idea that taking action can influence motivation and emotional state.

The tool encourages:

- acting without waiting for motivation
- reflecting on outcomes
- observing patterns over time through logged data


## Emotional Awareness

The tracker is more effective when feelings are described with specificity (e.g., using a feelings wheel) rather than broad terms.

More precise input improves the quality of the logged data and makes patterns easier to identify over time.

Example feelings wheel can be found here:

- [Exploring Marshall Rosenberg's Nonviolent Communication](https://www.solidgroundpsychiatry.com/post/the-power-of-compassionate-communication-exploring-marshall-rosenberg-s-nonviolent-communication)

