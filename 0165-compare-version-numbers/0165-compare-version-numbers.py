class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        ptr1 = 0
        ptr2 = 0
        version1_list = [int(elem) for elem in version1.split(".")]
        version2_list = [int(elem) for elem in version2.split(".")]
        
        
        while ptr1 < len(version1_list) and ptr2 < len(version2_list):
            if version1_list[ptr1] == version2_list[ptr2]:
                ptr1 += 1
                ptr2 += 1
            else:
                if version1_list[ptr1] > version2_list[ptr2]:
                    return 1
                else:
                    return -1
        
        if ptr1 != len(version1_list):
            while ptr1 < len(version1_list) and version1_list[ptr1] == 0:
                ptr1 += 1
            if ptr1 < len(version1_list):
                return 1
        if ptr2 != len(version2_list):
            while ptr2 < len(version2_list) and version2_list[ptr2] == 0:
                ptr2 += 1
            if ptr2 < len(version2_list):
                return -1
                
        return 0