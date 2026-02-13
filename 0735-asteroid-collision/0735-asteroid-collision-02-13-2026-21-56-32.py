class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # only collisions in which a is moving left and top of stack is moving right are the concern
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]

                if diff > 0:
                    # current asteroid is smaller, so explodes
                    a = 0 # mark as destroyed
                elif diff < 0:
                    # top of stack is bigger,  so explodes
                    stack.pop()
                    continue
                else:
                    # both equal
                    stack.pop()
                    a = 0

                # current asteroid is destroyed or neutralised
                break

            if a:
                stack.append(a)
        
        return stack