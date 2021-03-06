#NAME: Spencer Beatty
#ID: 260898452
import doctest
import time_series
import initial_clean
import matplotlib.pylab as plt

###############################################################
def round_to_five(x, base=5):
    return(base * round(float(x)/base))


#################################################################
class Patient:
    '''
    represents a patient
    
    Attributes: num, day_diagnosed, age, sex_gender, postal, state, temps, days_symptomatic

    >>> p = Patient('0', '0', '42', 'WOMAN', 'H3Z2B5', 'I', '102.2', '12')
    >>> print(str(p))
    0\t42\tW\tH3Z\t0\tI\t12\t39.00
    >>> p = Patient('0', '0', '42', 'BOY', '0', 'I', 'N/A', '12')
    >>> print(str(p))
    0\t42\tM\t000\t0\tI\t12\t0
    >>> p = Patient('0', '0', '42', 'NON-BINARY', 'H3Z2B5', 'I', '34,3', '12')
    >>> print(str(p))
    0\t42\tX\tH3Z\t0\tI\t12\t34.30
    >>> p = Patient('0', '0', '42', 'Boy', 'H3Z2B5', 'I', '34,3 C', '12')
    >>> print(str(p))
    0\t42\tM\tH3Z\t0\tI\t12\t39.00
    '''
    def sex_genders(self):
        '''
        (str) -> str
        takes the sex_gender of a patient and turns it into either 'M', 'F' or 'X'
        '''
        sex = self.sex_gender
        sex_initial = sex[0]
        
        if sex_initial == 'H' or sex_initial == 'B' or sex_initial == 'M':
            self.sex_gender = 'M'
        if sex_initial == 'F' or sex_initial == 'G' or sex_initial == 'W':
            self.sex_gender = 'F'
        if sex_initial == 'N' or sex_initial == 'X':
            self.sex_gender = 'X'
        
        return '{}'.format(self.sex_gender)

    def post(self):
        '''
        (str) -> str
        takes a postal code and returns the first three letters, if postal
        code is not applicable return 000
        '''
        post = self.postal
        if len(post) < 3:
            return '000'
        
        if post[0].isalpha() and post[1].isdigit() and post[2].isalpha():
            new_post = str(post[0]) + str(post[1]) + str(post[2])
            self.postal = str(new_post)
            return '{}'.format(self.postal)
        else:
            return '000'

    def temperature(self):
        '''
        (str) -> str
        takes a temperature and converts it into a standard float string in Celsius
        Things to look out for:
        French comma used for decimal points
        If the temp is in Farenheight convert it to Celsius, round to two decimals.
        (any temp above 45 is Farenheight
        If the string does not contain a number the Temp is 0
        '''
        temp = self.temps
        t = temp.split(';')
        temp = t[-1]
        del t[-1]
        
        

        saved_values = ''
        for i in t:
            saved_values += i
            saved_values += ';'
                
        
        
        counter = 0
        for i in temp:
            if i.isdigit():
                counter += 1
        if counter == 0:
            return '0'
        
        temp = temp.replace(',', '.')
        temp = temp.replace('-', '.')
        temp = temp.replace(' ', '')
        temp = temp.replace('C', '')
        temp = temp.replace('F', '')
        temp = temp.replace('°', '')


        if float(temp) > 45:
            temp = (float(temp) - 32) * 5/9
            temp = ("{0:.2f}".format(temp))

        self.temps = saved_values + temp
            
        return "{}".format(self.temps)

    def symptoms(self):
        day = self.days_symptomatic
        s = ''
        for i in day:
            if i.isdigit():
                s += i
            else:
                pass
            
                
            
        return  s 
    
    def __init__(self, num, day_diagnosed, age, sex_gender, postal, state, temps, days_symptomatic):
        self.num = int(num)
        self.day_diagnosed = int(day_diagnosed)
        self.age = int(age)
        self.sex_gender = sex_gender
        self.sex_gender = self.sex_genders()
        self.postal = postal
        self.postal = self.post()
        self.postal = self.post()
        self.state = state
        self.temps = temps
        self.days_symptomatic = days_symptomatic
        self.days_symptomatic = self.symptoms()

    

                         
    def __str__(self):
        '''
        >>> p = Patient('0', '0', '42', 'Boy', 'H3Z2B5', 'I', '34,3 C', '12')
        >>> print(str(p))
        0\t42\tM\tH3Z\t0\tI\t12\t34,3 C
        '''
        string = ''
        string += str(self.num)
        string += '\t'
        string += str(self.age)
        string += '\t'
        string += self.sex_gender
        string += '\t'
        string += self.postal
        string += '\t'
        string += str(self.day_diagnosed)
        string += '\t'
        string += self.state
        string += '\t'
        string += str(self.days_symptomatic)
        string += '\t'
        string += self.temps
        return string

    def update(self, self2):
        '''
        Things to check:
        update days symptomatic
        update state of patient
        append new temp to the end of patient 1
        Raise an AssertionError exception if num/sexgender/postal are not the same
        '''
        #if self.num != self2.num:
            #raise AssertionError('different number')
            
        #if self.sex_genders() != self2.sex_genders():
            #raise AssertionError('different sex_gender')
            
        #if self.post() != self2.post():
            #raise AssertionError('different postal')

        self.days_symptomatic = self2.days_symptomatic
        self.state = self2.state
        self.temps +=  ';' + self2.temperature()
        

        
patient_1 = Patient('0', '0', '42', 'N', 'H3Z2B5', 'I', '34.3 C;34.7', '12')    
patient_2 = Patient('0', '0', '42', 'N', 'H3Z2B5', 'I', '34.2 C', '12')



def stage_four(input_file, output_file):
    '''
    opens input_file reads it line by line, create a new patient line for each line.
    keep and return a dictionary of all patient lines,
    use the patients number as the key everything else as the values.
    whenever a new entry for an existing patient is seen update the entry.
    write it all to the output_file
    
    >>> stage_four('short_stage3.tsv', 'short_stage4.tsv')
    
    stage_four('long_stage3.tsv', 'long_stage4.tsv')

    stage_four('edge1_stage3.tsv', 'edge1_stage4.tsv')

    stage_four('edge2_stage3.tsv', 'edge2_stage4.tsv')
    
    '''
    
    file = open(input_file, 'r', encoding = 'utf-8')
    list_file = (file.readlines())
    file.close()

    patient_list = []
    for i in list_file:
        patient_list.append(i.split('\t'))
    
    patient_dict = {}
    
    organized_list = []
    for i in patient_list:
        for j in i:
            if j == i[1]:
                num = j
            if j == i[2]:
                day_diagnosed = j
            if j == i[3]:
                age = j
            if j == i[4]:
                sex_gender = j
            if j == i[5]:
                postal = j
            if j == i[6]:
                state = j
            if j == i[7]:
                temps = j
            if j == i[8]:
                days_symptomatic = j

        patient = Patient(num, day_diagnosed, age, sex_gender, postal, state, temps, days_symptomatic)        

        if i[0] in patient_dict:
            patient_dict[i[0]].update(patient)
        else: 
            patient_dict[i[0]] = patient

    return patient_dict
            


def fatality_by_age(patient_dict):
    '''
    (dict) -> plot
    create a plot using the data from the dict
    >>> p = stage_four('short_stage3.tsv', 'short_stage4.tsv')
    >>> fatality_by_age(p)
    '''
    age_list = []
    state_list = []
    for i in patient_dict:
        value = patient_dict[i]
        age = round_to_five(value.age)
        print(age)
        
        state = value.state

        
        
        age_list.append(age)
        state_list.append(state)
    

    print(age_list)
    age_nums = []
    for i in age_list:
        if i not in age_nums:
            age_nums.append(i)
        else:
            pass
    print(age_nums)
    
    age_death_dict = {}
    death_count = 0
    age_recov_dict = {}
    recovery_count = 0
    for pos, i in enumerate(age_nums):
        for j in age_list:
            if i == j:
                if state_list[pos] == 'D':
                    death_count += 1
                if state_list[pos] == 'R':
                    recovery_count += 1

            
            age_death_dict[j] = death_count
            age_recov_dict[j] = recovery_count
    
    

        



if __name__ == '__main__':
    doctest.testmod()
