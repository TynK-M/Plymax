class GameState():
    def __init__(self):
        """
        Layout used
        56 57 58 59 60 61 62 63
        48 49 50 51 52 53 54 55
        40 41 42 43 44 45 46 47
        32 33 34 35 36 37 38 39
        24 25 26 27 28 29 30 31
        16 17 18 19 20 21 22 23
        08 09 10 11 12 13 14 15
        00 01 02 03 04 05 06 07
        """
        # White pieces (Capital letter)
        self.P = 0b1111111100000000 # White pawn
        self.R = 0b10000001 # White Rook
        self.N = 0b1000010 # White Knight
        self.B = 0b100100 # White Bishop
        self.Q = 0b1000 # White Queen
        self.K = 0b10000 # White King
        # Black pieces (Small letter)
        self.p = 0b11111111000000000000000000000000000000000000000000000000 # Black pawn
        self.r = 0b1000000100000000000000000000000000000000000000000000000000000000 # Black Rook
        self.n = 0b100001000000000000000000000000000000000000000000000000000000000 # Black Knight
        self.b = 0b10010000000000000000000000000000000000000000000000000000000000 # Black Bishop
        self.q = 0b100000000000000000000000000000000000000000000000000000000000 # Black Queen
        self.k = 0b1000000000000000000000000000000000000000000000000000000000000 # Black King
        
        self.whiteToMove = True # White always moves first
        self.moveLog = [] # Keep track of moves