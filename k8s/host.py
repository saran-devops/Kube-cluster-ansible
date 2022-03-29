#!/usr/bin/python3  
import json  #ansible can understand easily

try:
    import boto3       #used to connect aws
except Exception as e:
    print("please check boto module is installed or not\n if not then use 'pip3 install boto3' ")
    print(e)
# we are getting IPs and appending in list
def get_hosts(ec2_ob, fv):   
    f={"Name":"tag:Name", "Values": [fv]}
    hosts=[]

    for each in ec2_ob.instances.filter(Filters=[f]):
        hosts.append(each.public_ip_address)
    return hosts




def main():
    ec2_ob=boto3.resource("ec2","us-east-2")   #checking ec2 info in ap-south-1 region
    
    
    k8s_master=get_hosts(ec2_ob, 'master')   # sending tag like master o find public IP
    k8s_slave=get_hosts(ec2_ob,'slave')      
    
    
    all_IPs={'master': k8s_master,'slave': k8s_slave }  # converting list into json so that ansible can understand
    
    print(json.dumps(all_IPs))      
    


if __name__=="__main__":
    main()
