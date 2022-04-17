    def read(self, project = '', sort =True): #함수 만들기
        if project=='': #project가 ''면
            if sort: #sort면
                sorted = self.df.sort_values('일정', ascending=False) #일정 오르는 순서 = False
                return sorted #저장
            else:
                return self.df #저장
        else:
            contain1 = self.df.프로젝트.str.contains(project, case=False) #프로젝트에 있으면 = contain1
            contain2 = self.df.Task.str.contains(project, case=False) #task에 있으면 = contain1
            contain3 = self.df.책임자.str.contains(project, case=False) #책임자에 있으면 = contain1
            contain = contain1 | contain2 | contain3
            if sort: #sort면
                sorted = self.df[contain].sort_values('일정', ascending=False) #일정 오르는 순서 = False
                return sorted #저장
            else: #아니면
                return self.df[contain] #저장