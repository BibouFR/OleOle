# OleOle

def collision(self,rect):
    if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
        if rect[1] < self.hitbox[3] +self.hitbox[1] and rect[1] + rect[3] > self.hitbox[1]:
            print("1 : ",rect[1] + rect[3])
            print("2 : ",self.hitbox[1] + self.hitbox[3]/2)
            print("3 : ",self.hitbox[1] -50)
            print("\n")


            if ((rect[1] + rect[3]) <= (self.hitbox[1] + self.hitbox[3]/2)) and ((rect[1] + rect[3]) >= (self.hitbox[1] -50)) :
                poele.y = self.hitbox[1] - 5 - poele.height
                print("yeeeeeeeeeees",self.hitbox[1])
                poele.isJump = False
                poele.jumpCount = 10

            if rect[0] < self.hitbox[0]:  #collision a droite
                poele.x -= 5
            elif rect[0] + rect[2] > self.hitbox[0]:
                poele.x += 5


            return True
    elif poele.y - poele.height != sol.y:
        poele.y = sol.y -poele.height
    return False
