import pygame
import os
from typing import List, Tuple

class Animator:
    """Handles animation sequences for Bonzi Buddy character."""
    
    def __init__(self, sprite_path: str):
        self.sprite_path = sprite_path
        self.frames: List[pygame.Surface] = []
        self.current_frame = 0
        self.animation_speed = 5
        self.is_playing = False
        
    def load_frames(self) -> None:
        """Load animation frames from sprite directory."""
        if os.path.exists(self.sprite_path):
            files = sorted(os.listdir(self.sprite_path))
            for file in files:
                if file.endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        frame = pygame.image.load(os.path.join(self.sprite_path, file))
                        self.frames.append(frame)
                    except pygame.error as e:
                        print(f"Error loading frame {file}: {e}")
    
    def play(self) -> None:
        """Start animation playback."""
        self.is_playing = True
        self.current_frame = 0
    
    def stop(self) -> None:
        """Stop animation playback."""
        self.is_playing = False
    
    def update(self) -> pygame.Surface:
        """Update animation frame and return current frame."""
        if not self.is_playing or not self.frames:
            return self.frames[0] if self.frames else None
        
        self.current_frame += 1
        if self.current_frame >= len(self.frames) * self.animation_speed:
            self.current_frame = 0
        
        return self.frames[self.current_frame // self.animation_speed]
    
    def set_animation_speed(self, speed: int) -> None:
        """Set animation speed (higher = faster)."""
        self.animation_speed = max(1, speed)