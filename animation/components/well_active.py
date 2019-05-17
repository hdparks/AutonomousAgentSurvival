class WellActive():
    def __init__(self, active=True, frameDelay=4):
        self.active = active
        self.cooldown = self.frameDelay = frameDelay
