import random
strategy_name = "Analyzing opponents' patterns and choosing the only choice left when given opponent's previous move choice and my previous move choice."
#There was probably an easier way to do this as well as a way to condense this...
def move(my_history, their_history):
  possible_moves = ["r", "p", "s"]
  my_move = ""
  my_move = random.choice(possible_moves)
  if len(their_history):
    if len(their_history) > 0:
      if their_history[-1] in "rps":
        if "rprp" == their_history[-4:] or "prpr" == their_history[-4:]:
          if their_history[-1] == "r":
            my_move = "s"
          else:
            my_move = "p"
        elif "rsrs" == their_history[-4:] or "srsr" == their_history[-4:]:
          if their_history[-1] == "r":
            my_move = "r"
          else:
            my_move = "p"
        elif "psps" == their_history[-4:] or "spsp" == their_history[-4:]:
          if their_history[-1] == "p":
            my_move = "r"
          else:
            my_move = "s"
        elif "pppp" == their_history[-4:] or "rrrr" == their_history[-4:] or "ssss" == their_history[-4:]:
          if their_history[-1] == "p":
            my_move = "s"
          elif their_history[-1] == "r":
            my_move = "p"
          else:
            my_move = "r"
        elif "rpsr" == their_history[-4:] or "rspr" == their_history[-4:]:
          if "sr" == their_history[-2:]:
            my_move = "s"
          elif "pr" == their_history[-2:]:
            my_move = "r"
          elif "ps" in their_history[-2:] or "sp" == their_history[-2:]:
            my_move = "p"
        elif "psrp" == their_history[-4:] or "prsp" == their_history[-4:]:
          if "rp" == their_history[-2:]:
            my_move = "r"
          elif "sp" == their_history[-2:]:
            my_move = "p"
          elif "sr" == their_history[-2:] or "rs" == their_history[-2:]:
            my_move = "s"
        elif "srps" == their_history[-4:] or "sprs" == their_history[-4:]:
          if "ps" == their_history[-2:]:
            my_move = "p"
          elif "rs" == their_history[-2:]:
            my_move = "s"
          elif "rp" == their_history[-2:] or "pr" == their_history[-2:]:
            my_move = "r"
        else:
          if my_history[-1] == "p":
            my_move = "r"
            #my_move = random.choice(["r", "s"])
          elif my_history[-1] == "s":
            my_move = "p"
            #my_move = random.choice(["r", "p"])
          elif my_history[-1] == "r":
            my_move = "s"
            #my_move = random.choice(["p", "s"])
  return my_move
