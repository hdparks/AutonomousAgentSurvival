class AgentActive():
    def __init__(self,active=True,frameDelay = 10):
        self.active = active
        self.frameDelay = self.cooldown = frameDelay
