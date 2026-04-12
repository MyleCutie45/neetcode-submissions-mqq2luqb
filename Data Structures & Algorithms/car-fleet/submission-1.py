class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mapo = []
        for i in range(len(speed)):
            mapo.append([position[i],(target-position[i])/speed[i]])
        cars = sorted(mapo,key=lambda x : (x[0],x[1]), reverse=True)
        stack =  []
        for pos,time in cars:
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)