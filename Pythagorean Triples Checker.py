'''

Pythagorean Triples
A "Pythagorean Triple" is a set of positive integers, a, b and c that fits the rule:

a*a + b*b = c*c

Here is a list of the first few Pythagorean Triples

(3,4,5)

(5,12,13)

Example: scale 3,4,5 by 2 gives 6,8,10 which should be Pythagorean Triples

'''

def PyTriples(a,b,c):

     asquare=a*a
     bsquare=b*b
     csquare=c*c
     if asquare+bsquare==csquare:
         print("Yes its a Pythagorean Triple\n")
         print("{} + {} = {}".format(asquare,bsquare,csquare) )

     else:
         print("Nopes! Its not a Pythagorean Triple")
         print("{} + {} is not = {}".format(asquare, bsquare, csquare))



def main():
    print("Check if a triangle is Pythagorean triples")

    a = int(input("input first integer a"))
    b = int(input("input second integer b"))
    c = int(input("input third integer c"))

    PyTriples(a, b, c)

    again=input("Wanna Try again? y/n")
    if again=='y':
        main()
    else:
        print("Goodbye! Thanks for using this app")

if __name__=="__main__": main()