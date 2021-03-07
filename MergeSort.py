def MergeSort(l):
    """
    given a list of integers sorts them
    in O(n log n) time.
    """
    def Merge(left,right):
        """
        s
        """
        merged = []
        i = 0
        j = 0
        
        while (i<len(left) and j<len(right)):
            if (left[i]>right[j]):
                merged.append(right[j])
                j+=1
            else:
                merged.append(left[i])
                i+=1
        if(i==len(left)):
            while (j<len(right)):
                merged.append(right[j])
                j+=1
        else:
            while(i<len(left)):
                merged.append(left[i])
                i+=1
        return merged

    left = l[len(l)//2:]
    right = l[:len(l)//2]

    if((len(left) or len(right))>1):
        left = MergeSort(left)
        right = MergeSort(right)
    merged=Merge(left,right)
    return merged

