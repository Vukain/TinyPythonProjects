class Settings:
    """Storing all settings"""

    def __init__(self):
        """Init game static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        # Ship settings

        self.ship_limit = 3
        # Alien settings

        self.fleet_drop_speed = 10

        # Bullet settings

        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        # How quickly the game speeds up
        self.speedup_scale = 1.5
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change during the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0
        # Fleet direction @ 1 is right, -1 is left
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
