class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    
    def power(self):
        self.__status = not self.__status

    
    def mute(self):
        """Mute or unmute the TV if it is on."""
        if self.__status:
            self.__muted = not self.__muted

    
    def channel_up(self):
        """Increase the channel by 1. If the max channel is reached, goes to the min channel."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    
    def channel_down(self):
        """Decrease the channel by 1. If the min channel is reached, goes to the max channel."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """Increase the volume by 1, unmuting the TV if necessary. Volume stays at max if it is already at max."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decrease the volume by 1, unmuting the TV if necessary. Volume stays at min if it is already at min."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"