-- 1)retrive all incident whose address is in 'Gardens'
select id
from fireincident 
where Location like'%Gardens%';


-- 2)retrive all incident whose nature of fire is heat 'transfer'
select id
from fireincident 
where natureOfFire='heat transfer';

-- 3)retrive all name firefighter whether they have a team or not
select f.name,f.firefigterTeamId
from firefighter f left outer join firefigterteam t on t.id=f.firefigterTeamId;

-- 4)retrive all name firefighter in team alpha 
select f.name 
from firefighter f,firefigterteam t
where t.name='alpha' and t.id=f.firefigterTeamId;

-- 5)retrive training certification those who participated fire loaction nile corniche
select f.trainingCertification
from firefighter f,firefigterteam t,fireincident i
where f.firefigterTeamId=t.id and t.id=i.firefigterTeamId and i.Location='nile corniche';

-- 6)retrive all incidents whose category fire classA
select id
from fireincident 
where  categoryFireIncident='class A';

-- 7)retrive specialized skills for firefighter whose in team bravo
 select f.specializedSkills
 from firefighter f,firefigterteam t
 where t.name='bravo' and f.firefigterTeamId=t.id;
 
 -- 8)retrive name of team who severity assessment 
select t.name
from firefigterteam t,fireincident i
where t.id=i.firefigterTeamId and incidentSeverityAssessment='Burn severity';
 
 -- 9)retrive name of team have equipment nozzle 
 select t.name 
 from firefighter f,firefigterteam t 
 where f.firefigterTeamId=t.id and f.availableEquipment='nozzle';
 
 -- 10)retrive training certification who in team delta
 select f.trainingCertification
 from firefighter f,firefigterteam t
 where f.firefigterTeamId=t.id and t.name ='delta';
 
 -- 11) People named ahmed
select * from demographicinformation d 
where d.name Like '%Ahmed%'  ;

-- 12) Males
select * from  demographicinformation d
where d.sex ='M' ;

-- 13) Females
select * from  demographicinformation d
where d.sex ='F' ;

-- 14) Details of visit
select d.name , m.detailsofvisit  AS details_of_visit from  demographicinformation d , medicalvisits m
where m.patient_ssn=d.ssn ;

-- 15) Details of past treatments
select d.name , m.pasttreatments  AS Past_Treatments from  demographicinformation d , medicalhistory m
where m.patient_ssn=d.ssn ;

-- 16) People with no allergies
select d.name from  demographicinformation d , allergies a 
where 
a.patientSpecificAllergies like '%None%'
and  a.patient_ssn=d.ssn ;

-- 17) Prescriptions
select d.name , p.name as 'Given By',warnings  from demographicinformation d , provider p , prescription b
where 
b.Provider_ID=p.ID
and
b.demographicInfronation_SSN=d.ssn ;

-- 18) The area where there was an oxygen fire
select location 
from fireincident 
where natureOfFire='Oxygen';

-- 19) Names of people who received a certificate
select Name
from firefighter
where trainingCertification like'%EMT%';

-- 20) retrive teamid People assigned to stairs
select firefigterTeamId
from  firefighter 
where availableEquipment='Ladder';