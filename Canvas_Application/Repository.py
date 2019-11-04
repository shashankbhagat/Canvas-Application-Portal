"""
File Name: Repository.py
Author: Bhavana Vankhede
Date: 12/14/2018
Notes: This implementation file serves as the Repository of the SQL statements.
"""
import DataAccess as da

class ComposeSQL:
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)
    
    def verifyUser(self,Text_UID,Text_pwd):
        self.query="select 1 from Login where username=? and password=?"
        self.parameter=(Text_UID,Text_pwd,)
        print(self.parameter)       
        obj=da.DbAccess()        
        record=obj.getSingleAnswer(self.query,self.parameter)
        #role=obj.getSingleAnswer(self.query_roles, self.parameter)
        #print('verify role', myRole)
        if record is not None:
            return True
        else:
            return False

    def peopleList(self):           #returns the list of people enrolled for this course along with the faculty member.
            self.query="""select Faculty,'Faculty' from Courses where CourseName='Python Programming'
            union all
            select s.FirstName||' '||s.LastName,'Student' from Course_Enrollment ce inner join Student s on (ce.StudentID=s.ID)
            where ce.courseName='Python Programming'"""
            obj=da.DbAccess()
            record=obj.getMultipleAnswers(self.query)
            return record

    def updatePeopleList(self,CourseCode,CourseName,Credits,StudentID):           #returns the list of people enrolled for this course along with the faculty member.
            self.query ="Insert into Course_Enrollment values (?,?,?,?) "
            self.parameter=('12','ds',12,11111,)
            obj=da.DbAccess()
            print('in rep:',self.query,self.parameter)
            obj.insertUpdateDelete(self.query,self.parameter)


    def listAssignments(self,studentID):            #returns the list of assignments for the course. 
        print(studentID)
        self.query="select roles from Login where username =?"
        self.parameter=(studentID,)
        obj=da.DbAccess()        
        role=obj.getSingleAnswer(self.query,self.parameter)
        print('role',role)
        if (role[0] == 'S'):
            self.query="""select ca.name,ca.duedate,ca.file from course_assignment ca 
            inner join  course_enrollment ce on (ca.coursename=ce.coursename) 
            where ce.studentid=?"""
            self.parameter=(studentID,)
            obj=da.DbAccess()
            record=obj.getMultipleAnswers(self.query,self.parameter)
            return record
        elif(role[0]=='A'):
            self.query="""select ca.name,ca.duedate,ca.file from course_assignment ca 
            inner join  course_enrollment ce on (ca.coursename=ce.coursename) 
            where ce.studentid=?"""
            self.parameter=(studentID,)
            obj=da.DbAccess()
            record=obj.getMultipleAnswers(self.query,self.parameter)
            return record
            

    def listFiles(self,studentID):              #returns the list of study material/files for the course.
        print(studentID)
        self.query="select roles from Login where username =?"
        self.parameter=(studentID,)
        obj=da.DbAccess()        
        role=obj.getSingleAnswer(self.query,self.parameter)
        print('role',role)
        if (role[0] == 'S'):
            self.query="""select cf.desc,cf.filename from course_files cf
            inner join  course_enrollment ce on (cf.coursename=ce.coursename) 
            where ce.studentid=?"""
            self.parameter=(studentID,)
            obj=da.DbAccess()
            record=obj.getMultipleAnswers(self.query,self.parameter)
            return record
        elif(role[0]=='A'):
            self.query="""select cf.desc,cf.filename from course_files cf
            inner join  course_enrollment ce on (cf.coursename=ce.coursename) 
            where ce.studentid=?"""
            self.parameter=(studentID,)
            obj=da.DbAccess()
            record=obj.getMultipleAnswers(self.query,self.parameter)
            return record
            

    
    def getGrades(self,studentID):          #returns the grades for the course.
        print(studentID)
        self.query="select roles from Login where username =?"
        self.parameter=(studentID,)
        obj=da.DbAccess()        
        role=obj.getSingleAnswer(self.query,self.parameter)
        print('role',role)
        if (role[0] == 'S'):
            self.query="""select name,duedate,marks,outof from grades where studentId=?"""
            self.parameter=(studentID,)
            obj=da.DbAccess()
            record=obj.getMultipleAnswers(self.query,self.parameter)
            return record
        elif(role[0]=='A'):
            self.query="""select name,duedate,marks,outof from grades where studentId=?"""
            self.parameter=(studentID,)
            obj=da.DbAccess()
            record=obj.getMultipleAnswers(self.query,self.parameter)
            return record

    def getAnnouncement(self):
        self.query="select Ann_date , desc from Announcement"
        obj= da.DbAccess()
        record = obj.getMultipleAnswers(self.query)
        return record
        