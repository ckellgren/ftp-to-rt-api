import requests
import atexit
import urllib
import sys
import os
import csv

## Connects to ReviewTrackers API
r = requests.post('https://api.reviewtrackers.com/auth', headers={
    'content-type': 'application/vnd.rtx.v2.hal+json;charset=utf-8',
    'accept': 'application/hal+json',
}, auth=('username', 'password'))

response= r.json()

TOKEN = response['token']

REQUESTS = [
    {
    'source': '***********/1023_O%27BrienToyotaScion_SL.CSV',
    'dealer_name': 'O\'Brien Toyota',
    'location': '598a965ceda1241df2c4dbcd',
    'template': '59c27b9c491772388fa9fea2',
    'sms': False, #email
    'autoselect': False,
    'urls': [
        '59b2e184fc80ab126592ad18',
        '598a965ca751d679bb7fc599',
        '598a965d5dc0547a6da2658b',
    ],
    },    
    {
    'source': '***********/1023_O%27BrienToyotaScion_SV.CSV',
    'dealer_name': '\'Brien Toyota',
    'location': '598a965ceda1241df2c4dbcd',
    'template': '59c27b9c491772388fa9fea2',
    'sms': False, #email
    'autoselect': False,
    'urls': [
        '59b2e184fc80ab126592ad18',
        '598a965ca751d679bb7fc599',
        '598a965d5dc0547a6da2658b',
    ],
    },    
    {
    'source': '***********/1024_TomO%27BrienChryslerJeepDodgeRamIndianapolis_SL.CSV',
    'dealer_name': 'Tom O\'Brien Indianapolis',
    'location': '598aa36a71253f198db39910',
    'template': '59cc1e183c1f2152db4cc4d4',
    'sms': False, #email
    'autoselect': False,
    'urls': [
        '598aa36b40d1ca148b080290',
        '598aa36a7dac447ae12d8ca8',
        '598aa36b0ceb6b0b186c6d09',
    ],
    },    
    {
    'source': '***********/1024_TomO%27BrienChryslerJeepDodgeRamIndianapolis_SV.CSV',
    'dealer_name': 'Tom O\'Brien Indianapolis',
    'location': '598aa36a71253f198db39910',
    'template': '59cc1e183c1f2152db4cc4d4',
    'sms': False, #email
    'autoselect': False,
    'urls': [
        '598aa36b40d1ca148b080290',
        '598aa36a7dac447ae12d8ca8',
        '598aa36b0ceb6b0b186c6d09',
    ],
    },    
    {
    'source': '***********/1027_TomO%27BrienChryslerJeepDodgeRamGreenwood_SL.CSV',
    'dealer_name': 'Tom O\'Brien Greenwood',
    'location': '598aa36580c8100d2ab483f7',
    'template': '59cc1da23c1f2152db4cc4d3',
    'sms': False, #email
    'autoselect': False,
    'urls': [
        '598aa366b053387e3b401fbf',
        '598aa365edd89c79bb133beb',
        '598aa3663752a70d293cacc0',
    ],
    },    
    {
    'source': '***********/1027_TomO%27BrienChryslerJeepDodgeRamGreenwood_SV.CSV',
    'dealer_name': 'Tom O\'Brien Greenwood',
    'location': '598aa36580c8100d2ab483f7',
    'template': '59cc1da23c1f2152db4cc4d3',
    'sms': False, #email
    'autoselect': False,
    'urls': [
        '598aa366b053387e3b401fbf',
        '598aa365edd89c79bb133beb',
        '598aa3663752a70d293cacc0',
    ],
    },       
    {
    'source': '***********/2111_LouisvilleInfiniti_SL.CSV',
    'dealer_name': 'Louisville Infiniti',
    'location': '598a2577bdb82e7a344d3d46',
    'template': '59bc37963d164504d147cc6a',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/2111_LouisvilleInfiniti_SV.CSV',
    'dealer_name': 'Louisville Infiniti',
    'location': '598a2577bdb82e7a344d3d46',
    'template': '59bc37963d164504d147cc6a',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/24_AudiMelbourne_SL.CSV',
    'dealer_name': 'Audi of Melbourne',
    'location': '5989c902efac2961e5fa66d4',
    'template': '59bc399b3d164504d147cc6f',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/24_AudiMelbourne_SV.CSV',
    'dealer_name': 'Audi of Melbourne',
    'location': '5989c902efac2961e5fa66d4',
    'template': '59bc399b3d164504d147cc6f',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/319_MazdaofSouthCharlotte_SL.CSV',
    'dealer_name': 'Mazda of South Charlotte',
    'location': '598a2548af8b350412e11e94',
    'template': '59bc3b723d164504d147cc72',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/319_MazdaofSouthCharlotte_SV.CSV',
    'dealer_name': 'Mazda of South Charlotte',
    'location': '598a2548af8b350412e11e94',
    'template': '59bc3b723d164504d147cc72',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/42_PorscheofMelbourne_SL.CSV',
    'dealer_name': 'Porsche of Melbourne',
    'location': '598a966958196f147c4e6821',
    'template': '59bc3b223d164504d147cc71',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/42_PorscheofMelbourne_SV.CSV',
    'dealer_name': 'Porsche of Melbourne',
    'location': '598a966958196f147c4e6821',
    'template': '59bc3b223d164504d147cc71',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/47_MercedesBenzofMelbourne_SL.CSV',
    'dealer_name': 'Mercedes-Benz of Melbourne',
    'location': '598a256192e9297fef27dd06',
    'template': '59bc3a993d164504d147cc70',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/47_MercedesBenzofMelbourne_SV.CSV',
    'dealer_name': 'Mercedes-Benz of Melbourne',
    'location': '598a256192e9297fef27dd06',
    'template': '59bc3a993d164504d147cc70',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/53_InfinitiofCoolSprings_SL.CSV',
    'dealer_name': 'Infiniti of Cool Springs',
    'location': '5989e500d79be87b505e4f73',
    'template': '59bc38113d164504d147cc6b',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/53_InfinitiofCoolSprings_SV.CSV',
    'dealer_name': 'Infiniti of Cool Springs',
    'location': '5989e500d79be87b505e4f73',
    'template': '59bc38113d164504d147cc6b',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/59_LakeNormanInfiniti_SL.CSV',
    'dealer_name': 'Lake Norman Infiniti',
    'location': '598a1d969315ff7fef87f2ea',
    'template': '59bc37343d164504d147cc69',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/59_LakeNormanInfiniti_SV.CSV',
    'dealer_name': 'Lake Norman Infiniti',
    'location': '598a1d969315ff7fef87f2ea',
    'template': '59bc37343d164504d147cc69',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/658_ToyotaofDenton_SL.CSV',
    'dealer_name': 'Toyota of Denton',
    'location': '598a8dade2ea707ff0b5b077',
    'template': '59bc393a3d164504d147cc6e',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/658_ToyotaofDenton_SV.CSV',
    'dealer_name': 'Toyota of Denton',
    'location': '598a8dade2ea707ff0b5b077',
    'template': '59bc393a3d164504d147cc6e',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/660_HondaofDenton_SL.CSV',
    'dealer_name': 'Honda of Denton',
    'location': '5989e204a9fc097b19a3c90d',
    'template': '59bc3bcc3d164504d147cc73',
    'sms': False, #email
    'autoselect': False,
    'urls': [
        '5989e207d6f85e7addf5b7ee',
        '5989e206a754117be3ed7a1e',
        '5989e205565aaf797b6262fd',
    ],
    },    
    {
    'source': '***********/660_HondaofDenton_SV.CSV',
    'dealer_name': 'Honda of Denton',
    'location': '5989e204a9fc097b19a3c90d',
    'template': '59bc3bcc3d164504d147cc73',
    'sms': False, #email
    'autoselect': False,
    'urls': [
        '5989e207d6f85e7addf5b7ee',
        '5989e206a754117be3ed7a1e',
        '5989e205565aaf797b6262fd',
    ],
    },    
    {
    'source': '***********/98_LakeNormanHyundai_SL.CSV',
    'dealer_name': 'Lake Norman Hyundai',
    'location': '598a255676d54f19a41d8f0c',
    'template': '59bc38923d164504d147cc6d',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/98_LakeNormanHyundai_SV.CSV',
    'dealer_name': 'Lake Norman Hyundai',
    'location': '598a255676d54f19a41d8f0c',
    'template': '59bc38923d164504d147cc6d',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/2314_BedfordNissan_SL.CSV',
    'dealer_name': 'Bedford Nissan',
    'location': '5989cca1aaaf754c499ac350',
    'template': '59a8822e5e1765db5a3e5fb0',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/2314_BedfordNissan_SV.CSV',
    'dealer_name': 'Bedford Nissan',
    'location': '5989cca1aaaf754c499ac350',
    'template': '59a8822e5e1765db5a3e5fb0',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },    
    {
    'source': '***********/2313_MentorNissan_SL.CSV',
    'dealer_name': 'Mentor Nissan',
    'location': '598a256f15f050147caa6480',
    'template': '59a884415e1765db5a3e5fb2',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2313_MentorNissan_SV.CSV',
    'dealer_name': 'Mentor Nissan',
    'location': '598a256f15f050147caa6480',
    'template': '59a884415e1765db5a3e5fb2',
    'sms': False, #email
    'autoselect': True,
    'urls': [],
    },
    {
    'source': '***********/2282_FremontToyotaSheridan_SL.CSV',
    'dealer_name': 'Fremont Toyota Sheridan',
    'location': '598a1d761ed570198d4649c1',
    'template': '599ef9e1112390554486f39c',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2282_FremontToyotaSheridan_SV.CSV',
    'dealer_name': 'Fremont Toyota Sheridan',
    'location': '598a1d761ed570198d4649c1',
    'template': '599ef9e1112390554486f39c',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1936_O%27BrienAutoPark_SL.CSV',
    'dealer_name': 'O%27Brien Auto Park',
    'location': '599f0f56e5ffa11ab8b77098',
    'template': '599f12c7c882d67e4d4b2976',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1936_O%27BrienAutoPark_SV.CSV',
    'dealer_name': 'O%27Brien Auto Park',
    'location': '599f0f56e5ffa11ab8b77098',
    'template': '599f12c7c882d67e4d4b2976',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1242_MajorWorldChryslerDodgeJeepRam_SL.CSV',
    'dealer_name': 'Major World CDJR',
    'location': '59a86819c67c1706729dfd17',
    'template': '599df22d3049490791792ac5',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1242_MajorWorldChryslerDodgeJeepRam_SV.CSV',
    'dealer_name': 'Major World CDJR',
    'location': '59a86819c67c1706729dfd17',
    'template': '599df22d3049490791792ac5',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/898_BasneyImports_SL.CSV',
    'dealer_name': 'Basney Imports',
    'location': '5989cc98b4ba636bfe23e6fb',
    'template': '599de45b3049490791792a98',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/898_BasneyImports_SV.CSV',
    'dealer_name': 'Basney Imports',
    'location': '5989cc98b4ba636bfe23e6fb',
    'template': '599de45b3049490791792a98',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/136_AcuraofPembrokePines_SL.CSV',
    'dealer_name': 'Acura of Pembroke Pines',
    'location': '5989cc9b43cdb36b80cee9af',
    'template': '599de2b13049490791792a8b',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/136_AcuraofPembrokePines_SV.CSV'
    'dealer_name': 'Acura of Pembroke Pines',
    'location': '5989cc9b43cdb36b80cee9af',
    'template': '599de2b13049490791792a8b',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1516_MiniofBedford_SL.CSV',
    'dealer_name': 'Mini of Bedford',
    'location': '598a254b898b7f7982975a73',
    'template': '599df3c892ee3c6d9fec74e1',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1516_MiniofBedford_SV.CSV',
    'dealer_name': 'Mini of Bedford',
    'location': '598a254b898b7f7982975a73',
    'template': '599df3c892ee3c6d9fec74e1',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1518_AcuraofPeabody_SL.CSV',
    'dealer_name': 'Acura of Peabody',
    'location': '5989c90b876fd5498f965d97',
    'template': '599c47733dd20b12450edafd',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1518_AcuraofPeabody_SV.CSV',
    'dealer_name': 'Acura of Peabody',
    'location': '5989c90b876fd5498f965d97',
    'template': '599c47733dd20b12450edafd',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1519_JaguarofPeabody_SL.CSV',
    'dealer_name': 'Jaguar of Peabody',
    'location': '5989e90675eea57add7e0117',
    'template': '599efa81112390554486f3a0',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1519_JaguarofPeabody_SV.CSV',
    'dealer_name': 'Jaguar of Peabody',
    'location': '5989e90675eea57add7e0117',
    'template': '599efa81112390554486f3a0',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1522_BMWofPeabody_SL.CSV',
    'dealer_name': 'BMW of Peabody',
    'location': '5989d831a7601e797b849325',
    'template': '599eefce112390554486f38d',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1522_BMWofPeabody_SV.CSV',
    'dealer_name': 'BMW of Peabody',
    'location': '5989d831a7601e797b849325',
    'template': '599eefce112390554486f38d',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1824_MarinoChryslerJeepDodgeRAM_SL.CSV',
    'dealer_name': 'Marino CDJR',
    'location': '598a256df09a2c797b20de74',
    'template': '599df24b3049490791792ac6',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1824_MarinoChryslerJeepDodgeRAM_SV.CSV',
    'dealer_name': 'Marino CDJR',
    'location': '598a256df09a2c797b20de74',
    'template': '599df24b3049490791792ac6',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2123_NationalDodgeChryslerJeepRAM_SL.CSV',
    'dealer_name': 'National Dodge Chrysler Jeep RAM',
    'location': '598aa374f3fe3a7e3bc37d47',
    'template': '599df43d92ee3c6d9fec74e4',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2123_NationalDodgeChryslerJeepRAM_SV.CSV',
    'dealer_name': 'National Dodge Chrysler Jeep RAM',
    'location': '598aa374f3fe3a7e3bc37d47',
    'template': '599df43d92ee3c6d9fec74e4',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2266_FremontMotorLanderFordChryslerDodgeJeepRam_SL.CSV',
    'dealer_name': 'Fremont Motor Lander',
    'location': '598a0f3d6452f37a893a421d',
    'template': '599ef9a1112390554486f399',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2266_FremontMotorLanderFordChryslerDodgeJeepRam_SV.CSV',
    'dealer_name': 'Fremont Motor Lander',
    'location': '598a0f3d6452f37a893a421d',
    'template': '599ef9a1112390554486f399',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2267_FremontMotorCodyFordLincolnandChryslerDodge_SL.CSV',
    'dealer_name': 'Fremont Motor Cody',
    'location': '598a0f4700060878c29d3ec1',
    'template': '599ef029112390554486f390',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2267_FremontMotorCodyFordLincolnandChryslerDodge_SV.CSV',
    'dealer_name': 'Fremont Motor Cody',
    'location': '598a0f4700060878c29d3ec1',
    'template': '599ef029112390554486f390',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2268_FremontMotorSheridanFordLincoln_SL.CSV',
    'dealer_name': 'Fremont Motor Sheridan',
    'location': '598a1da5cfde88797ba7f06e',
    'template': '59a9a66893b428af886c68a5',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2268_FremontMotorSheridanFordLincoln_SV.CSV',
    'dealer_name': 'Fremont Motor Sheridan',
    'location': '598a1da5cfde88797ba7f06e',
    'template': '59a9a66893b428af886c68a5',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2269_FremontMotorRockSpringsChryslerDodgeJeepRam_SL.CSV',
    'dealer_name': 'Fremont Motor Rock Springs',
    'location': '598a0f2c84ba24797bb76751',
    'template': '599ef0c3112390554486f395',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2269_FremontMotorRockSpringsChryslerDodgeJeepRam_SV.CSV',
    'dealer_name': 'Fremont Motor Rock Springs',
    'location': '598a0f2c84ba24797bb76751',
    'template': '599ef0c3112390554486f395',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2270_FremontMotorPowellFordLincolnChryslerDodgeJee_SL.CSV',
    'dealer_name': 'Fremont Motor Powell',
    'location': '598a0f37005758146a2b587f',
    'template': '599ef061112390554486f392',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2270_FremontMotorPowellFordLincolnChryslerDodgeJee_SV.CSV',
    'dealer_name': 'Fremont Motor Powell',
    'location': '598a0f37005758146a2b587f',
    'template': '599ef061112390554486f392',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2272_FremontMotorRivertonFordLincoln_SL.CSV',
    'dealer_name': 'Fremont Motor Riverton',
    'location': '598a0f32908fe9148bf06865',
    'template': '599ef07a112390554486f393',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2272_FremontMotorRivertonFordLincoln_SV.CSV',
    'dealer_name': 'Fremont Motor Riverton',
    'location': '598a0f32908fe9148bf06865',
    'template': '599ef07a112390554486f393',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2274_FremontMotorCasperChryslerDodgeJeepRam_SL.CSV',
    'dealer_name': 'Fremont Motor Casper',
    'location': '5989e8fc52d8937a8b0c4739',
    'template': '599eefef112390554486f38e',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2274_FremontMotorCasperChryslerDodgeJeepRam_SV.CSV',
    'dealer_name': 'Fremont Motor Casper',
    'location': '5989e8fc52d8937a8b0c4739',
    'template': '599eefef112390554486f38e',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2275_FremontVolkswagenCasper_SL.CSV',
    'dealer_name': 'Fremont Volkswagen',
    'location': '598a1d699cd9917cfc6609c6',
    'template': '599efa01112390554486f39d',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2275_FremontVolkswagenCasper_SV.CSV',
    'dealer_name': 'Fremont Volkswagen',
    'location': '598a1d699cd9917cfc6609c6',
    'template': '599efa01112390554486f39d',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2278_FremontToyotaLander_SL.CSV',
    'dealer_name': 'Fremont Toyota Lander',
    'location': '598a1da2c4b0e27ad66a6225',
    'template': '599ef9c9112390554486f39b',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2278_FremontToyotaLander_SV.CSV',
    'dealer_name': 'Fremont Toyota Lander',
    'location': '598a1da2c4b0e27ad66a6225',
    'template': '599ef9c9112390554486f39b',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2440_ToyotaofBristol_SL.CSV',
    'dealer_name': 'Toyota of Bristol',
    'location': '598a9677ad25f67a34191bb6',
    'template': '599df7b292ee3c6d9fec74f5',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2440_ToyotaofBristol_SV.CSV',
    'dealer_name': 'Toyota of Bristol',
    'location': '598a9677ad25f67a34191bb6',
    'template': '599df7b292ee3c6d9fec74f5',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/248_NickAlexanderBMW_SL.CSV',
    'dealer_name': 'Nick Alexander BMW',
    'location': '598a998dd801837a8b343b37',
    'template': '599df47192ee3c6d9fec74e5',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/248_NickAlexanderBMW_SV.CSV',
    'dealer_name': 'Nick Alexander BMW',
    'location': '598a998dd801837a8b343b37',
    'template': '599df47192ee3c6d9fec74e5',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2506_MarthalerChryslerDodgeJeepRAM_SL.CSV',
    'dealer_name': 'Marthaler CDJR',
    'location': '598a256a57a96f0528141dd7',
    'template': '599df2633049490791792ac7',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2506_MarthalerChryslerDodgeJeepRAM_SV.CSV',
    'dealer_name': 'Marthaler CDJR',
    'location': '598a256a57a96f0528141dd7',
    'template': '599df2633049490791792ac7',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2513_KeyesHyundai_SL.CSV',
    'dealer_name': 'Keyes Hyundai',
    'location': '598a255a144cf305281d9736',
    'template': '599df05f3049490791792aba',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2513_KeyesHyundai_SV.CSV',
    'dealer_name': 'Keyes Hyundai',
    'location': '598a255a144cf305281d9736',
    'template': '599df05f3049490791792aba',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2523_StephenWadeToyota_SL.CSV',
    'dealer_name': 'Stephen Wade Toyota',
    'location': '598a99917589b67cdaea346d',
    'template': '599df62d92ee3c6d9fec74f0',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2523_StephenWadeToyota_SV.CSV',
    'dealer_name': 'Stephen Wade Toyota',
    'location': '598a99917589b67cdaea346d',
    'template': '599df62d92ee3c6d9fec74f0',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2944_BellRoadToyota_SL.CSV',
    'dealer_name': 'Bell Road Toyota',
    'location': '5989ce625fc2046c01239870',
    'template': '599eef3c112390554486f38c',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2944_BellRoadToyota_SV.CSV',
    'dealer_name': 'Bell Road Toyota',
    'location': '5989ce625fc2046c01239870',
    'template': '599eef3c112390554486f38c',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2558_KeyesMissionHillsHyundai_SL.CSV',
    'dealer_name': 'Keyes Mission Hills Hyundai',
    'location': '598a1d9d42e78a19a4f7397f',
    'template': '599df0863049490791792abd',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2558_KeyesMissionHillsHyundai_SV.CSV',
    'dealer_name': 'Keyes Mission Hills Hyundai',
    'location': '598a1d9d42e78a19a4f7397f',
    'template': '599df0863049490791792abd',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2602_KennyKentToyota_SL.CSV',
    'dealer_name': 'Kenny Kent Toyota',
    'location': '5989e9009d80017b8f5a4bfb',
    'template': '599df01b3049490791792ab9',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2602_KennyKentToyota_SV.CSV',
    'dealer_name': 'Kenny Kent Toyota',
    'location': '5989e9009d80017b8f5a4bfb',
    'template': '599df01b3049490791792ab9',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/261_ToyotaofNewnan_SL.CSV',
    'dealer_name': 'Toyota of Newnan',
    'location': '598a966451de9119bbaf1380',
    'template': '599df7cd92ee3c6d9fec74f6',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/261_ToyotaofNewnan_SV.CSV',
    'dealer_name': 'Toyota of Newnan',
    'location': '598a966451de9119bbaf1380',
    'template': '599df7cd92ee3c6d9fec74f6',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2271_FremontChevyBuickGMC_SL.CSV',
    'dealer_name': 'Fremont Chevy Buick GMC',
    'location': '598a011f474a537be36b1ca3',
    'template': '599ef00d112390554486f38f',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2271_FremontChevyBuickGMC_SV.CSV',
    'dealer_name': 'Fremont Chevy Buick GMC',
    'location': '598a011f474a537be36b1ca3',
    'template': '599ef00d112390554486f38f',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2905_FredMartinSuperstore_SL.CSV',
    'dealer_name': 'Fred Martin Superstore',
    'location': '5989e20cc470a27b18ecd975',
    'template': '599dec5b3049490791792ab1',
    'sms': True #sms
    'autoselect': False,
    'urls': [
        '5989e20eb278ee7ade59752b',
        '5989e20fd3aff27ade2ce8b4',
    ],
    },
    {   
    'source': '***********/2905_FredMartinSuperstore_SV.CSV',
    'dealer_name': 'Fred Martin Superstore',
    'location': '5989e20cc470a27b18ecd975',
    'template': '599dec5b3049490791792ab1',
    'sms': True #sms
    'autoselect': False,
     'urls': [
        '5989e20eb278ee7ade59752b',
        '5989e20fd3aff27ade2ce8b4',
    ],
    },
    {   
    'source': '***********/2908_FredMartinNissan_SL.CSV',
    'dealer_name': 'Fred Martin Nissan',
    'location': '5989e2109537e97b196918b1',
    'template': '599dec243049490791792aaf',
    'sms': True #sms
    'autoselect': False,
    'urls': [
        '5989e212ec65c77a8c26c116',
        '5989e215e8246f7a74338da9',
    ],
    },
    {   
    'source': '***********/2908_FredMartinNissan_SV.CSV',
    'dealer_name': 'Fred Martin Nissan',
    'location': '5989e2109537e97b196918b1',
    'template': '599dec243049490791792aaf',
    'sms': True #sms
    'autoselect': False,
    'urls': [
        '5989e212ec65c77a8c26c116',
        '5989e215e8246f7a74338da9',
    ],
    },
    {   
    'source': '***********/2912_LibertyKia_SL.CSV',
    'dealer_name': 'Liberty Kia',
    'location': '598a1d703a19dd7ae12ff7c1',
    'template': '599df1993049490791792ac1',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2912_LibertyKia_SV.CSV',
    'dealer_name': 'Liberty Kia',
    'location': '598a1d703a19dd7ae12ff7c1',
    'template': '599df1993049490791792ac1',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2912_LibertyNissan_SL.CSV',
    'dealer_name': 'Liberty Nissan',
    'location': '598a1d6412338d05c4c381d0',
    'template': '599df1d43049490791792ac3',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2912_LibertyNissan_SV.CSV',
    'dealer_name': 'Liberty Nissan',
    'location': '598a1d6412338d05c4c381d0',
    'template': '599df1d43049490791792ac3',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2912_LibertyVolkswagen_SL.CSV',
    'dealer_name': 'Liberty Volkswagen',
    'location': '598a1d604bd64719bc266801',
    'template': '599df1ea3049490791792ac4',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/2912_LibertyVolkswagen_SV.CSV',
    'dealer_name': 'Liberty Volkswagen',
    'location': '598a1d604bd64719bc266801',
    'template': '599df1ea3049490791792ac4',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/3078_MercedToyota_SL.CSV',
    'dealer_name': 'Merced Toyota',
    'location': '598a254e90a0d8146ac851a0',
    'template': '599df36b3049490791792ac9',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/3078_MercedToyota_SV.CSV',
    'dealer_name': 'Merced Toyota',
    'location': '598a254e90a0d8146ac851a0',
    'template': '599df36b3049490791792ac9',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/308_BobSmithToyota_SL.CSV',
    'dealer_name': 'Bob Smith Toyota',
    'location': '598a9666844eb97cfb869df0',
    'template': '59a48f28b80905756601f2f8',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/308_BobSmithToyota_SV.CSV',
    'dealer_name': 'Bob Smith Toyota',
    'location': '598a9666844eb97cfb869df0',
    'template': '59a48f28b80905756601f2f8',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/478_CoppusMotors_SL.CSV',
    'dealer_name': 'Coppus Motors',
    'location': '598a0f425f8f587ad1c2e81c',
    'template': '599de7fb3049490791792aa6',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/478_CoppusMotors_SV.CSV',
    'dealer_name': 'Coppus Motors',
    'location': '598a0f425f8f587ad1c2e81c',
    'template': '599de7fb3049490791792aa6',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/688_WestbornChryslerDodgeJeepRam_SL.CSV',
    'dealer_name': 'Westborn CDJR',
    'location': '598aa36c8514f77a8b989abe',
    'template': '599df7fb92ee3c6d9fec74f8',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/688_WestbornChryslerDodgeJeepRam_SV.CSV',
    'dealer_name': 'Westborn CDJR',
    'location': '598aa36c8514f77a8b989abe',
    'template': '599df7fb92ee3c6d9fec74f8',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/83_BobSmithMINI_SL.CSV',
    'dealer_name': 'Bob Smith MINI',
    'location': '5989d81ef907b361e332851e',
    'template': '599de4e53049490791792a9c',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/83_BobSmithMINI_SV.CSV',
    'dealer_name': 'Bob Smith MINI',
    'location': '5989d81ef907b361e332851e',
    'template': '599de4e53049490791792a9c',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/842_RosevilleCDJR_SL.CSV',
    'dealer_name': 'Roseville CDJR',
    'location': '598aa372768b2719bc217cc8',
    'template': '599df60792ee3c6d9fec74ef',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/842_RosevilleCDJR_SV.CSV',
    'dealer_name': 'Roseville CDJR',
    'location': '598aa372768b2719bc217cc8',
    'template': '599df60792ee3c6d9fec74ef',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/8_BobSmithBMW_SL.CSV',
    'dealer_name': 'Bob Smith BMW',
    'location': '5989d825f323376693e30df9',
    'template': '599de4b83049490791792a9b',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/8_BobSmithBMW_SV.CSV',
    'dealer_name': 'Bob Smith BMW',
    'location': '5989d825f323376693e30df9',
    'template': '599de4b83049490791792a9b',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/90_NickAlexanderMINI_SL.CSV',
    'dealer_name': 'Nick Alexander MINI',
    'location': '598aa3684427fa7add87e2d8',
    'template': '599df48592ee3c6d9fec74e6',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/90_NickAlexanderMINI_SV.CSV',
    'dealer_name': 'Nick Alexander MINI',
    'location': '598aa3684427fa7add87e2d8',
    'template': '599df48592ee3c6d9fec74e6',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/972_OrangeCoastChryslerJeepDodge_SL.CSV',
    'dealer_name': 'Orange Coast CDJR',
    'location': '598aa3700a9bd91dd295f704',
    'template': '599df4fa92ee3c6d9fec74eb',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/972_OrangeCoastChryslerJeepDodge_SV.CSV',
    'dealer_name': 'Orange Coast CDJR',
    'location': '598aa3700a9bd91dd295f704',
    'template': '599df4fa92ee3c6d9fec74eb',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/981_LampeChryslerDodgeJeepRam_SL.CSV',
    'dealer_name': 'Lampe CDJR',
    'location': '598a1d8f655e9c7a3491f0ac',
    'template': '599df0fe3049490791792abf',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/981_LampeChryslerDodgeJeepRam_SV.CSV',
    'dealer_name': 'Lampe CDJR',
    'location': '598a1d8f655e9c7a3491f0ac',
    'template': '599df0fe3049490791792abf',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/850_ElkoMotorCompanyCDJR_SL.CSV',
    'dealer_name': 'Elko Motor Company',
    'location': '5989cc9f88b8bb61e7971715',
    'template': '599deb953049490791792aac',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/850_ElkoMotorCompanyCDJR_SV.CSV',
    'dealer_name': 'Elko Motor Company',
    'location': '5989cc9f88b8bb61e7971715',
    'template': '599deb953049490791792aac',
    'sms': True #sms
    'autoselect': True,
    'urls': [],
    },
     {   
    'source': '***********/1807_FullertonCDJR_SL.CSV',
    'dealer_name': 'Fullerton CDJR',
    'location': '5989c8fdd6250061e4683b4b',
    'template': '599decb03049490791792ab2',
    'sms': True, #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1807_FullertonCDJR_SV.CSV',
    'dealer_name': 'Fullerton CDJR',
    'location': '5989c8fdd6250061e4683b4b',
    'template': '599decb03049490791792ab2',
    'sms': True, #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1822_FullertonFIAT_SL.CSV',
    'dealer_name': 'Fullerton FIAT',
    'location': '5989ce6b650790497d634f0f',
    'template': '599ded143049490791792ab4',
    'sms': True, #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1822_FullertonFIAT_SV.CSV',
    'dealer_name': 'Fullerton FIAT',
    'location': '5989ce6b650790497d634f0f',
    'template': '599ded143049490791792ab4',
    'sms': True, #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1823_FullertonFord_SL.CSV',
    'dealer_name': 'Fullerton Ford',
    'location': '5989cca49fd5a96693422668',
    'template': '599ded643049490791792ab5',
    'sms': True, #sms
    'autoselect': True,
    'urls': [],
    },
    {   
    'source': '***********/1823_FullertonFord_SV.CSV',
    'dealer_name': 'Fullerton Ford',
    'location': '5989cca49fd5a96693422668',
    'template': '599ded643049490791792ab5',
    'sms': True, #sms
    'autoselect': True,
    'urls': [],
    },
]

## Searches source files for Recipient data
def getRecipients(source='', sms=True):
    try:
        rows = list(csv.DictReader(urllib.urlopen(source)))[1:]
    except IOError:
        print "file not found: {}".format(source)
        return

    recipients = []

    if sms:
        for row in rows:
            got_dat_phone = False
            contact_info_count = 0
            final_value = False
            for col in [
                'CustomerCellPhone',
                'CustomerHomePhone',
            ]:
                try:
                    value = row[col].strip()
                except KeyError:
                    value = False

                if col in ['CustomerCellPhone'] and value:
                    final_value = value
                
                if not final_value and col in ['CustomerHomePhone'] and value:
                    final_value = value

            if final_value: 
                recipients.append(final_value)
    else:
        for row in rows:
            try:
                value = row['CustomerEmail'].strip()
            except KeyError:
                value = False

            if value:
                recipients.append(value)

    return recipients

## Payload for the request
for request in REQUESTS:
    payload = {
        'sender_name': request['dealer_name'],
        'sender_email': 'no.reply@automotive-dealers.reviews', # Sender Email is hardcoded
        'status': 'publish',
        'recipients': getRecipients(
            source=request['source'],
            sms=request['sms']
        ),
        'location_id': request['location'],
        'template_id': request['template'],
        'account_id': '5988b386630e954983aea8b4', # Account ID is hardcoded
    }

    print payload

    if request['autoselect']:
        payload['auto_select_sources'] = 'true'
    else:
        payload['url_ids'] = request['urls']

## Sends campaigns using Recipient data and location data from REQUESTS
    response = requests.post('https://api.reviewtrackers.com/campaigns', headers={
        'accept': 'application/json',
    }, json=payload, auth=('username', TOKEN))

    print response.json()

