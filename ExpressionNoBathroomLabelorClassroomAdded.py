# This label expression with classes also takes away the label of "classroom" and "bathroom", along with bathroom numbers

# Overrun set to 0 every class
# Placement = straight in polygon, try horizontal first
# Regular (not bold) font

# Class 1 - in beoynd None out beyond 1:500
def FindLabel([Shape__Area], [featnum], [featname],[type]):
    area = float([Shape__Area])
    baseFontSizeNum = 7
    baseFontSizeName =3
    scaleMultiplier = 0.05
    scaledFontSizeNum = baseFontSizeNum + (area * scaleMultiplier)
    scaledFontSizeName = baseFontSizeName + (area * scaleMultiplier)
    minFontSizeNum = 2
    minFontSizeName = 1
    maxFontSize = 10
    finalFontSizeNum = min(max(scaledFontSizeNum, minFontSizeNum), maxFontSize)
    finalFontSizeName = min(max(scaledFontSizeName, minFontSizeName), maxFontSize)
    type = [type]
    
    featname = ([featname])
    featnum = ([featnum])
    
    featname = featname.upper() if featname else None
    featnum = featnum.upper() if featnum else None
    
    featname_length = len(featname) if featname else 0
    featnum_length = len(featnum) if featnum else 0
    combined_length = featname_length + featnum_length
    
    if type == "bathroom":
        return None
    else:
        if combined_length * finalFontSizeName > area or combined_length * finalFontSizeNum > area:
            if featnum is not None:
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>"
            elif featnum is None:
                return "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
        else:
            if featname is not None and featnum is not None and featname != "ROOM" and featname != "CORRIDOR" and featname != "CLASSROOM":
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>\n<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featname == "CORRIDOR":
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>" + " " + "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featnum is not None and featname == "ROOM" or featname == "CLASSROOM":
                return "<FNT size='" + str(finalFontSizeNum) + " '>" + featnum + "</FNT>"
            elif featnum is None:
                return "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featname is None:
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>"

# Class 2 - in beyond 1:500 out beyond 1:725
def FindLabel([Shape__Area], [featnum], [featname],[type]):
    area = float([Shape__Area])
    baseFontSizeNum = 5
    baseFontSizeName =2
    scaleMultiplier = 0.05
    scaledFontSizeNum = baseFontSizeNum + (area * scaleMultiplier)
    scaledFontSizeName = baseFontSizeName + (area * scaleMultiplier)
    minFontSizeNum = 2
    minFontSizeName = 1
    maxFontSize = 10
    finalFontSizeNum = min(max(scaledFontSizeNum, minFontSizeNum), maxFontSize)
    finalFontSizeName = min(max(scaledFontSizeName, minFontSizeName), maxFontSize)
    type = [type]
    
    featname = ([featname])
    featnum = ([featnum])
    
    featname = featname.upper() if featname else None
    featnum = featnum.upper() if featnum else None
    
    featname_length = len(featname) if featname else 0
    featnum_length = len(featnum) if featnum else 0
    combined_length = featname_length + featnum_length
    
    if type == "bathroom":
        return None
    else:
        if combined_length * finalFontSizeName > area or combined_length * finalFontSizeNum > area:
            if featnum is not None:
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>"
            elif featnum is None:
                return "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
        else:
            if featname is not None and featnum is not None and featname != "ROOM" and featname != "CORRIDOR" and featname != "CLASSROOM":
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>\n<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featname == "CORRIDOR":
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>" + " " + "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featnum is not None and featname == "ROOM" or featname == "CLASSROOM":
                return "<FNT size='" + str(finalFontSizeNum) + " '>" + featnum + "</FNT>"
            elif featnum is None:
                return "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featname is None:
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>"

# Class 3 - in beyond 1:725 out beyond 1:1100
def FindLabel([Shape__Area], [featnum], [featname],[type]):
    area = float([Shape__Area])
    baseFontSizeNum = 4
    baseFontSizeName =2
    scaleMultiplier = 0.02
    scaledFontSizeNum = baseFontSizeNum + (area * scaleMultiplier)
    scaledFontSizeName = baseFontSizeName + (area * scaleMultiplier)
    minFontSizeNum = 2
    minFontSizeName = 1
    maxFontSize = 10
    finalFontSizeNum = min(max(scaledFontSizeNum, minFontSizeNum), maxFontSize)
    finalFontSizeName = min(max(scaledFontSizeName, minFontSizeName), maxFontSize)
    type = [type]
    
    featname = ([featname])
    featnum = ([featnum])
    
    featname = featname.upper() if featname else None
    featnum = featnum.upper() if featnum else None
    
    featname_length = len(featname) if featname else 0
    featnum_length = len(featnum) if featnum else 0
    combined_length = featname_length + featnum_length
    
    if type == "bathroom":
        return None
    else:
        if combined_length * finalFontSizeName > area or combined_length * finalFontSizeNum > area:
            if featnum is not None:
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>"
            elif featnum is None:
                return "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
        else:
            if featname is not None and featnum is not None and featname != "ROOM" and featname != "CORRIDOR" and featname != "CLASSROOM":
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>\n<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featname == "CORRIDOR":
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>" + " " + "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featnum is not None and featname == "ROOM" or featname == "CLASSROOM":
                return "<FNT size='" + str(finalFontSizeNum) + " '>" + featnum + "</FNT>"
            elif featnum is None:
                return "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featname is None:
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>"

# Clas 4 - in beoynd 1:1100 out beyond 1800
def FindLabel([Shape__Area], [featnum], [featname],[type]):
    area = float([Shape__Area])
    baseFontSizeNum = 4
    baseFontSizeName =1
    scaleMultiplier = 0.01
    scaledFontSizeNum = baseFontSizeNum + (area * scaleMultiplier)
    scaledFontSizeName = baseFontSizeName + (area * scaleMultiplier)
    minFontSizeNum = 2
    minFontSizeName = 1
    maxFontSize = 10
    finalFontSizeNum = min(max(scaledFontSizeNum, minFontSizeNum), maxFontSize)
    finalFontSizeName = min(max(scaledFontSizeName, minFontSizeName), maxFontSize)
    type = [type]
    
    featname = ([featname])
    featnum = ([featnum])
    
    featname = featname.upper() if featname else None
    featnum = featnum.upper() if featnum else None
    
    featname_length = len(featname) if featname else 0
    featnum_length = len(featnum) if featnum else 0
    combined_length = featname_length + featnum_length
    
    if type == "bathroom":
        return None
    else:
        if combined_length * finalFontSizeName > area or combined_length * finalFontSizeNum > area:
            if featnum is not None:
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>"
            elif featnum is None:
                return "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
        else:
            if featname is not None and featnum is not None and featname != "ROOM" and featname != "CORRIDOR" and featname != "CLASSROOM":
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>\n<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featname == "CORRIDOR":
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>" + " " + "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featnum is not None and featname == "ROOM" or featname == "CLASSROOM":
                return "<FNT size='" + str(finalFontSizeNum) + " '>" + featnum + "</FNT>"
            elif featnum is None:
                return "<FNT size='" + str(finalFontSizeName) + "'>" + featname + "</FNT>"
            elif featname is None:
                return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>"

# Class 5 - in beoynd 1800 out beyond None
def FindLabel([Shape__Area], [featnum], [featname], [type]):
    area = float([Shape__Area])
    baseFontSizeNum = 3
    scaleMultiplier = 0.01
    scaledFontSizeNum = baseFontSizeNum + (area * scaleMultiplier)
    minFontSizeNum = 2
    maxFontSize = 10
    finalFontSizeNum = min(max(scaledFontSizeNum, minFontSizeNum), maxFontSize)
    type = [type]
    
    featnum = ([featnum])
    featnum = featnum.upper() if featnum else None
    
    if type == "bathroom":
        return None
    else:
        if featnum is not None:
            return "<FNT size='" + str(finalFontSizeNum) + "'>" + featnum + "</FNT>"
        elif featnum is None:
            return None
