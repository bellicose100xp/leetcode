class Solution:
    def firstUniqChar(self, s: str) -> int:
        str_count: dict[str, dict[str, int]] = {}
        for idx, c in enumerate(s):
            val = str_count.get(c, {"count": 0, "index": -1})
            val["count"] += 1
            val["index"] = idx
            
            str_count[c] = val
        
        for key in str_count:
            if str_count[key]["count"] == 1:
                return str_count[key]["index"]
        
        return -1