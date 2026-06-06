class Solution:
    DELIMITER="##"

    def buildHeader(self, strs):
        lengths = [str(len(s)) for s in strs]
        return ",".join(lengths) + self.DELIMITER
    
    def getHeaderData(self, endodedString):
        data = endodedString.split(self.DELIMITER)[0]
        if len(data) < 1:
            return []
        return data.split(",")
    
    def buildPayload(self, strs):
        return "".join(strs)
    
    def getEncodedPayload(self, endodedString):
        ## TODO: consider error handling
        res = self.DELIMITER.join(endodedString.split(self.DELIMITER)[1:])
        return res

    def encode(self, strs: List[str]) -> str:
        return self.buildHeader(strs) + self.buildPayload(strs)

    def decode(self, s: str) -> List[str]:
        header = self.getHeaderData(s)
        payload = self.getEncodedPayload(s)
        res = []
        ptr = 0
        for l in header:
            size = int(l)
            entry = payload[ptr:(ptr+size)]
            res.append(entry)
            ptr+=size
        return res


