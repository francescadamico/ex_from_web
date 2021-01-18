'''
https://igotanoffer.com/blogs/tech/google-software-engineer-interview

Given a matrix of N rows and M columns. From m[i][j], we can move to m[i+1][j], if m[i+1][j] > m[i][j], or can move to m[i][j+1] if m[i][j+1] > m[i][j]. The task is print longest path length if we start from (0, 0).

'''
import numpy as np

def long_inc_path(m: list, path_summ = 0, max_path = 0) -> int:

  m_down = m[1][0] if len(m) > 1 else -1
  m_right = m[0][1] if len(m[0]) > 1 else -1

  if m_down < m[0][0] and m_right < m[0][0]:
    path_summ += 1
    max_path = path_summ if path_summ > max_path else max_path
   
    return max_path

  path_summ += 1 

  if m_down > m[0][0]:
    max_path = long_inc_path(np.delete(m, 0, 0), path_summ, max_path)  
  
  if m_right > m[0][0]:
    max_path = long_inc_path(np.delete(m, 0, 1), path_summ, max_path) 


  return max_path  



m = np.array([
    [1, 2, 3, 4 ],  
    [2, 2, 3, 4 ],  
    [3, 2, 3, 4 ],  
    [4, 5, 6, 7 ]
])


print(long_inc_path(m))
