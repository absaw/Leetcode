class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # max ip value : 255.255.255.255 
        # so string with length > 12 are invalid. return []
        # lowest = 0.0.0.0
        if len(s) < 4 or len(s) > 12:
            return []

        # s= "25525511135"
        # max len for each digit group is 3, 
        res = []
        def solution(curr_s,curr_idx,dots):
            if dots == 4 and curr_idx == len(s):
                res.append(curr_s[:-1])

            for i in range(1,4):
                new_idx = curr_idx+i
                if new_idx < len(s)+1:
                    segment = s[curr_idx:curr_idx+i]
                    if segment[0]=='0' and len(segment)!=1:
                        continue
                    if int(segment) < 256:
                        solution(curr_s+segment+".",new_idx,dots+1)
        solution("",0,0)
        return res

