# Habit Tracker

## Overview

A CLI habit tracker that logs emotional state before and after completing a task.

Designed to explore how taking action influences emotional state over time, based on principles from cognitive behavioral therapy (CBT) and behavioral activation.

---

## Purpose

This tool is built around a simple idea:

> motivation is not required to begin.

Instead of waiting to feel ready, users:
- record how they feel before starting  
- take action  
- reflect on how they feel afterward  

Over time, this creates a dataset that shows how action can change emotional state.

---

## Features

- CLI-based workflow (`start` / `end`)  
- Tracks:
  - habit  
  - feeling before  
  - activity performed  
  - feeling after  
  - session duration  
- Per-habit CSV logging  
- Session persistence using a temporary state file  

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

- Encourages acting without relying on motivation  
- Emphasizes reflection and feedback loops  
- Uses simple file-based storage for transparency and portability  

## Emotional Awareness

The tracker works best when feelings are named with specificity (e.g., using a feelings wheel) rather than broad terms.

This improves clarity in the data and helps identify patterns over time.

Example feelings wheel can be found here:

- [Exploring Marshall Rosenberg's Nonviolent Communication](https://www.solidgroundpsychiatry.com/post/the-power-of-compassionate-communication-exploring-marshall-rosenberg-s-nonviolent-communication)

---

