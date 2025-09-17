"""
You are given an integer array `heights` where `heights[i]` represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: heights = [1,8,6,2,5,4,8,3,7]
Output: 49

Heights: [1, 8, 6, 2, 5, 4, 8, 3, 7]

    0  1  2  3  4  5  6  7  8
    |  |  |  |  |  |  |  |  |

Bars (height) represented as vertical columns:

 8 |        #                 #         <--- Bar at index 1 (height=8) and index 6 (height=8)
 7 |                          #                    Bar at index 8 (height=7)
 6 |           #             
 5 |              #          
 4 |                 #       
 3 |                      # 
 2 |     #                  
 1 | #                      
   +-------------------------
    0  1  2  3  4  5  6  7  8
    
"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # formula = (l-r) * (min(heights[l],heights[r]))

        maxcapacity = 0
        l = 0
        r = len(heights)-1

        while l<r:
            cap = (r - l) * (min(heights[l],heights[r]))
            maxcapacity = max(maxcapacity,cap)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return maxcapacity
