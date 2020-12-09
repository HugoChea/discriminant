import random
import math

class Polynome :
    
    # Constructor : Define polynomial function as : f(x) = ax^2 + bx + c
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Calculate discrimant delta as : delta = b^2 - 4ac and return value
    def calculateDelta(self):
        delta = (self.b ** 2) - (4 * self.a * self.c)
        return delta

class Exercise :

    # Constructor : Define number of questions and initialize score
    def __init__(self, question_quantity):
        self.question_quantity = question_quantity
        self.score = 0

    # Function that start the exercise
    def start(self):
        print("Exercice sur les discriminants :\n")
        question_number = 1

        while question_number <= self.question_quantity :
            self.generateRandomQuestion()
            question_number = question_number + 1

        print("{}/{}".format(self.score, self.question_quantity))
        return True

    # Function that generate random question
    def generateRandomQuestion(self):
        rdm = random.randint(1, 4)
        if rdm == 1:
            self.squareDiscriminant()
        elif rdm == 2:
            self.negativeDiscriminant()
        elif rdm == 3:
            self.littleDiscrimant()
        elif rdm == 4:
            self.bigDiscrimant()

    # Function that generates a question : discrimant carré
    # delta = 1, 4,9, 16,25,36,49,64,81, 100
    # b > delta
    def squareDiscriminant(self):
        # the max square in this exercise
        square_range = 5
        array_number = [i for i in range(1, square_range)]
        
        # generate new array with all square values
        delta_square_array = [x**2 for x in array_number]
        # choose a random square value for delta
        rdm = random.randint(0, len(array_number)-1)
        delta = delta_square_array[rdm]
        # b is random, b^2 is at least equal to delta so b^2 > delta
        b = random.randint(array_number[rdm], array_number[rdm]+square_range)

        # delta = b^2 - 4ac
        # delta + 4ac = b^2
        # 4ac = b^2 - delta 
        # a*c = (b^2 - delta) /4
        ac = ((b ** 2) - delta) /4

        ## divisibility to find pair a, c
        diviseur = [2,3,4,5,6,7,8,9,10]
        index = 0
        divisibility = False

        while (divisibility == False and index < len(diviseur)) :
            if ac % diviseur[index] == 0 :
                a = diviseur[index]
                c = ac / a
                divisibility == True

            index = index + 1
        
        if divisibility == False :
            a = 1
            c = ac

        p = Polynome(a,b,c)
        value = int(p.calculateDelta())

        print("Trouver le discriminant de {}x^2+{}x+{} dont la réponse est {}".format(a,b,c, int(value)))
        print("Discriminant carré")
        response = input("Réponse : \n")
        if int(response) == int(value) :
            print("Correct")
            self.score = self.score + 1
            return True
        else :
            print("Non Correct")
            return False
    
    # Function that generates a question : discrimant petit < 20
    def littleDiscrimant(self):
        delta = random.randint(1, 19)
        if (delta != math.isqrt(delta) ** 2):
            delta = delta +1
        # delta = b^2 - 4ac
        # delta + 4ac = b^2
        # ac = (b^2 - delta) / 4
        b = random.randint(3, 10)
        # si b inférieur ou egal a delta, rajoute la difference à b
        if ((b**2) < delta):
            b = b + (delta - (b**2))
        # si b egal a delta, on ajoute 1
        if ((b**2) == delta):
            b = b + 1
        # make ac divisible par 4 en rajoutant le reste de la division par 4
        if ((b ** 2) - delta % 4 !=0) :
            delta = delta + (((b ** 2) - delta) % 4)

        # si delta trop grand, on le réduit en conservant la divisionabilité par 4
        if delta > 20 :
            delta = delta -4

        ac = int(((b ** 2) - delta)/4)

        # (b ** 2) - delta = 4
        if ac == 1:
            a = 1
            c = 1
        # (b ** 2) - delta = 0
        elif ac == 0:
            a = 0
            c = 0
        else :
            diviseur = []
            for i in range(1, ac):
                if (ac % i == 0) :
                    diviseur.append(i)
            
            random_index = random.randint(0, len(diviseur)-1)
            a = diviseur[random_index]
            c = ac / a

        p = Polynome(a,b,c)
        value = p.calculateDelta()

        print("Trouver le discriminant de {}x^2+{}x+{} dont la réponse est {}".format(a,b,c, int(value)))
        print("Discriminant non carré mais petit")
        response = input("Réponse : \n")
        if int(response) == int(value) :
            print("Correct")
            self.score = self.score + 1
            return True
        else :
            print("Non Correct")
            return False

    # Function that generates a question : discrimant grand > 20
    def bigDiscrimant(self):
        delta = random.randint(21, 100)
        if (delta != math.isqrt(delta) ** 2):
            delta = delta +1
        # delta = b^2 - 4ac
        # delta + 4ac = b^2
        # ac = (b^2 - delta) / 4
        b = random.randint(3, 10)
        # si b inférieur ou egal a delta, rajoute la difference à b
        if ((b**2) < delta):
            b = b + (delta - (b**2))
        # si b egal a delta, on ajoute 1
        if ((b**2) == delta):
            b = b + 1
        # make ac divisible par 4
        if ((b ** 2) - delta % 4 !=0) :
            delta = delta + (((b ** 2) - delta) % 4)

        if delta < 20 :
            delta = delta + 4

        ac = int(((b ** 2) - delta)/4)

        if ac == 1:
            a = 1
            c = 1
        elif ac == 0:
            a = 0
            c = 0
        else :
            diviseur = []
            for i in range(1, ac):
                if (ac % i == 0) :
                    diviseur.append(i)
            
            random_index = random.randint(0, len(diviseur)-1)
            a = diviseur[random_index]
            c = ac / a

        p = Polynome(a,b,c)
        value = p.calculateDelta()
        
        print("Trouver le discriminant de {}x^2+{}x+{} dont la réponse est {}".format(a,b,c, int(value)))
        print("Discriminant non carré mais grand")
        response = input("Réponse : \n")
        if int(response) == int(value) :
            print("Correct")
            self.score = self.score + 1
            return True
        else :
            print("Non Correct")
            return False

    # Function that generates a question : discrimant negatif
    def negativeDiscriminant(self):
        #4ac > b^2 and a > 0 and c > 0 and b > 1
        number_range = 5
        b = random.randint(2, number_range)
        b_square = b ** 2
        ac = int(random.randrange(b_square, b_square+number_range)/4)+1
        a = random.randint(1, ac)
        c = random.randint(1+(ac-a), ac)
        
        p = Polynome(a,b,c)
        value = p.calculateDelta()
        
        print("Trouver le discriminant de {}x^2+{}x+{} dont la réponse est {}".format(a,b,c, int(value)))
        print("Discriminant négatif")
        response = input("Réponse : \n")
        if int(response) == int(value) :
            print("Correct")
            self.score = self.score + 1
            return True
        else :
            print("Non Correct")
            return False


e = Exercise(10)
e.start()