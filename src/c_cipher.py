import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
def encrypt(email="abc012"):
    """
    TODO: What is the objective? 

    Args:
        TODO: what arguments and data types are expected? (i.e., email)

    Returns:
        TODO: what varibale and data types are being returned?   
    """
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = ((email[:3] != email[:3] and email[:3].isalpha())) or (email[3:] != email[3:] and email[3:].isdigit())

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # TODO: fix line below, process our string into a list
    email_lst = ' '.join(email)
    email_lst = email_lst.split(' ')
        
    # TODO: complete line(s) below, convert EACH new element into a string
    i = 0
    while i < len(email_lst):
        new_ascii = (ord(email_lst[i]) + 3) # NOTE: here we extract and update element at 0 
        email_lst[i] = chr(new_ascii)   # NOTE: here we convert our ASCII into string
        i += 1
        
    # TODO: fix line below, convert list into a string
    email_str = ''.join(email_lst)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    TODO: What is the objective? 

    Args:
        TODO: what arguments and data types are expected? (i.e., email)

    Returns:
        TODO: what varibale and data types are being returned?   
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = (email[:3] != email[:3]) or (email[3:] != email[3:]) 

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # TODO: apply the encrypt pseudocode but shift down 3
    email_lst = ' '.join(email)
    email_lst = email_lst.split(' ')
    i = 0
    while i < len(email_lst):
        new_ascii = (ord(email_lst[i]) - 3) # NOTE: here we extract and update element at 0 
        email_lst[i] = chr(new_ascii)   # NOTE: here we convert our ASCII into string
        i += 1
        
    email_str = ''.join(email_lst)
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal
