#!/usr/bin/env python
# coding: utf-8

# # BFS using python

# In[17]:


def bfs(g,begin):
    explored=[]
    frontier=[]
    explored.append(begin)
    frontier.append(begin)
    
    while frontier:
        n=frontier.pop(0)
        print(n)
        for i in g[n]:
            if i not in explored:
                explored.append(i)
                frontier.append(i)
                    
g={0:[1,2],1:[3],2:[3,4],3:[4],4:[0]}
bfs(g,0)


# # DFS WITH GOAL

# In[23]:


def dfs(g,begin,goal):
    explored=[]
    frontier=[]
    explored.append(begin)
    frontier.append(begin)
    while frontier:
        n=frontier.pop()
        print(n,'\n')
        if n==goal:
            print("found")
            break
        for i in g[n]:
            if i not in explored:
                explored.append(i)
                frontier.append(i)
                
g={0:[1,2],1:[3],2:[3,4],3:[4],4:[0]}
dfs(g,0,3)

