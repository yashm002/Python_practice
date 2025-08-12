# *args takes arguments in the form of tuple
# **kwargs takes arguments in the form of dictionary
def chess_shop(game, *peices, **check):
    print(f"The sports is {game} which consists of:")
    for items in peices:
        print(f"- {items}")
    print(check)


# peices = ["Pawn", "King", "Queen", "Bishop", "Knight", "Rook"]
# check = {"delivery: True", "Payment: Done"}
chess_shop("chess", "Pawn", "King", "Queen", "Bishop", "Knight", "Rook", delivery=True, Payment=True)
