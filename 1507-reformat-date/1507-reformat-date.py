class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", \
                 "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", \
                 "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        
        ans = []
        for new_date in date.split(" "):
            if new_date in month:
                ans.append(month[new_date])
            elif new_date[-1] not in "0123456789":
                temp = new_date[:-2]
                if len(temp) < 2:
                    temp = "0" + temp
                ans.append(temp)
            else:
                ans.append(new_date)
        
        return "-".join(ans[::-1])