##Calculator
#print("He Mad!");
#print("*" + "\n**" + "\n***");
Wat = 12;
Pat = 14;
Line = ["0"];
LinetoC = "1465";
Wat += Pat
#print(Wat);

print("Calulator Main Menu")
while 1:
        print("Current String: "+ str(Line[0]))
        print("Z to end")
        print("Numbers: 1 2 3 \n\t 4 5 6 \n\t 7 8 9")
        Number = int(input("Input: "))
        if Number == "Z":
                break;
        print("Conjunctions: + * - /")
        Conjunc = input("Input:")

        match Conjunc:
                case("+"):
                    Line[0] = int(Line[0], base=0) + Number;
                case("*"):
                    Line[0] = int(Line[0], base=0) * Number;
                case("-"):
                    Line[0] = int(Line[0], base=0) - Number;
                case("/"):
                    Line[0] = int(Line[0], base=0) / Number;
        Line[0] = str(Line[0])
        print(Line)
def Conjuncs(popacc, Conjunc):
      match Conjunc:
            case("+"):
                    Line[0] = int(Line[0], base=0) + Number;
            case("*"):
                    Line[0] = int(Line[0], base=0) * Number;
            case("-"):
                Line[0] = int(Line[0], base=0) - Number;
            case("/"):
                Line[0] = int(Line[0], base=0) / Number;
      popacc = 1
      return popacc;
