print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('''        /                            )
          (                             |\
         /|                              \\
        //                                \\
       ///                                 \|
      /( \                                  )\
      \\  \_                               //)
       \\  :\__                           ///
        \\     )                         // \
         \\:  /                         // |/
          \\ / \                       //  \
           /)   \   ___..-'           (|  \_|
          //     /   _.'              \ \  \
         /|       \ \________          \ | /
        (| _ _  __/          '-.       ) /.'
         \\ .  '-.__            \_    / / \
          \\_'.     > --._ '.     \  / / /
           \ \      \     \  \     .' /.'
            \ \  '._ /     \ )    / .' |
             \ \_     \_   |    .'_/ __/
              \  \      \_ |   / /  _/ \_
               \  \       / _.' /  /     \
               \   |     /.'   / .'       '-,_
                \   \  .'   _.'_/             \
   /\    /\      ) ___(    /_.'           \    |
  | _\__// \    (.'      _/               |    |
  \/_  __  /--'`    ,                   __/    /
  (_ ) /b)  \  '.   :            \___.-'_/ \__/
  /:/:  ,     ) :        (      /_.'__/-'|_ _ /
 /:/: __/\ >  __,_.----.__\    /        (/(/(/
(_(,_/V .'/--'    _/  __/ |   /
 VvvV  //`    _.-' _.'     \   \
   n_n//     (((/->/        |   /
   '--'         ~='          \  |
                              | |_,,,
                 snd          \  \  /
                               '.__)''')

direction = input("Which way do you go? left or right?\n").lower()#make the input lower case so any answer will be easily processable.
if direction == "left":
  wait_or_swim = input("You arrived to a lake. Wait or swim?\n").lower()
  if wait_or_swim == "wait":
    doors = input("You arrived to a room with 3 doors. Red, yellow and blue. Which one do you choose?\n").lower()
    if doors == "yellow":#Give the user different ways of game over with elif.
      print("You won!")
    elif doors == "red":
      print("Game Over. The room is on fire.")
    elif doors == "blue":
      print("Game Over. You froze in -100 celsius.")
  else:
    print("Game over. A crocodile ate you.")
else:
  print("Game over. You fell from the mountain.")