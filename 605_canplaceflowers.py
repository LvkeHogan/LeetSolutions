class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #"case for plot size 1"
        print("hi")
        if len(flowerbed) == 1 and flowerbed[0] == 0 or n == 0:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] != 0:
            return False
        #"for plots bigger than 1, find how many potential places you can plant.
        plantable = 0
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    plantable += 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    plantable += 1
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    plantable += 1
        if plantable >= n:
            return True
        else:
            return False