######733. Flood Fill####################################################################################################################
// Time Complexity : n
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : no problem

// Your code here along with comments explaining your approach in three sentences only
We have applied BFS by using the direction array where for start box we check the neighbors and color them with new color and further more relates boxes are colored


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        #print([sr,sc])
        #q1=collections.deque()
        r,c=len(image),len(image[0])
        dirlist=[[0,1],[1,0],[0,-1],[-1,0]]
        self.dfs(image, sr,sc, image[sr][sc], color, dirlist)
        return image

    def dfs(self,image,r,c,initcolor,color,dirlist):
        #base
        if (r<0 or c<0 or r==len(image) or c==len(image[0]) or image[r][c]!=initcolor):
            return

        image[r][c]=color
        #logic
        for i in dirlist:
            rn,cn=r+i[0],c+i[1]
            #print('rec start:',image)
            self.dfs(image,rn,cn,initcolor,color,dirlist)
            #print('rec end:',image)
        
        
        

######542. 01 Matrix############################################################################################################


// Time Complexity : n
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : NA

// Your code here along with comments explaining your approach in three sentences only
Here instead of considering 1 we consider 0 as starting point and also converted all 1 to -1 and apply BFS and found the -1 on next level and update as distance


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirlist=[[0,1],[1,0],[0,-1],[-1,0]]
        q1=collections.deque()
        r,c=len(mat),len(mat[0])
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    q1.append([i,j])
                if mat[i][j]==1:
                    mat[i][j]=-1
        lvl=1
        #print(q1)
        while len(q1)>0:
            len1=len(q1)
            for j in range(len1):
                cur=q1.popleft()
                curr,curc=cur[0],cur[1]
                #print(curr,curc)
                for i in dirlist:
                    nr,nc=curr+i[0],curc+i[1]
                    #print('in for loop:',nr,nc)
                    if nr>=0 and nc>=0 and nr<r and nc<c and mat[nr][nc]==-1:
                        #print(nr,nc,lvl)
                        q1.append([nr,nc])
                        mat[nr][nc]=lvl
            lvl+=1
        #print(mat)
        return mat

        