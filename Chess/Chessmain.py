class GameState():
    def __init__(self):
        """
        Code representation of the board.
        First letter : color
        ┣━━ b = Black
        ┗━━ w = White
        Second letter : piece
        ┣━━ p = Pawn
        ┣━━ Q = Queen
        ┣━━ K = King
        ┣━━ B = Bishop
        ┣━━ N = Knight
        ┗━━ R = Rook
        """
        self.board = [                       
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"] # 8
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"] # 7
            ["--", "--", "--", "--", "--", "--", "--", "--"] # 6
            ["--", "--", "--", "--", "--", "--", "--", "--"] # 5
            ["--", "--", "--", "--", "--", "--", "--", "--"] # 4
            ["--", "--", "--", "--", "--", "--", "--", "--"] # 3
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"] # 2  
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"] # 1
            # a     b     c     d     e     f     g     h
        ]
        self.whiteToMove = True # White always moves first
        self.moveLog = [] # Keep track of moves