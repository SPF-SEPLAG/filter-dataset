def add_tipo_column(df):
    tipo_map = {
        # Fornecimento
        3001: "Fornecimento", 3002: "Fornecimento", 3003: "Fornecimento", 3004: "Fornecimento",
        3005: "Fornecimento", 3006: "Fornecimento", 3007: "Fornecimento", 3008: "Fornecimento",
        3009: "Fornecimento", 3010: "Fornecimento", 3011: "Fornecimento", 3012: "Fornecimento",
        3013: "Fornecimento", 3014: "Fornecimento", 3015: "Fornecimento", 3016: "Fornecimento",
        3017: "Fornecimento", 3018: "Fornecimento", 3019: "Fornecimento", 3020: "Fornecimento",
        3021: "Fornecimento", 3022: "Fornecimento", 3023: "Fornecimento", 3024: "Fornecimento",
        3025: "Fornecimento", 3026: "Fornecimento", 3027: "Fornecimento", 3028: "Fornecimento",
        3029: "Fornecimento", 3030: "Fornecimento", 3031: "Fornecimento", 3032: "Fornecimento",
        3033: "Fornecimento", 3034: "Fornecimento", 3035: "Fornecimento", 3036: "Fornecimento",
        3037: "Fornecimento", 3038: "Fornecimento", 3039: "Fornecimento", 3040: "Fornecimento",
        3041: "Fornecimento", 3042: "Fornecimento", 3099: "Fornecimento", 3101: "Fornecimento",
        3102: "Fornecimento", 3103: "Fornecimento", 3104: "Fornecimento", 3105: "Fornecimento",
        5201: "Fornecimento", 5202: "Fornecimento", 5203: "Fornecimento", 5204: "Fornecimento",
        5205: "Fornecimento", 5206: "Fornecimento", 5207: "Fornecimento", 5208: "Fornecimento",
        5209: "Fornecimento", 5210: "Fornecimento", 5211: "Fornecimento", 5212: "Fornecimento",
        5213: "Fornecimento", 5214: "Fornecimento", 5215: "Fornecimento", 5216: "Fornecimento",
        5217: "Fornecimento", 5218: "Fornecimento", 5219: "Fornecimento", 5220: "Fornecimento",
        5221: "Fornecimento", 5222: "Fornecimento", 5223: "Fornecimento", 5224: "Fornecimento",
        5225: "Fornecimento", 5226: "Fornecimento", 5227: "Fornecimento", 5230: "Fornecimento",
        5299: "Fornecimento",

        # Serviço
        3301: "Serviço", 3302: "Serviço", 3303: "Serviço", 3304: "Serviço", 3305: "Serviço",
        3401: "Serviço", 3402: "Serviço", 3403: "Serviço", 3404: "Serviço", 3405: "Serviço",
        3501: "Serviço", 3502: "Serviço", 3503: "Serviço",
        3601: "Serviço", 3602: "Serviço", 3603: "Serviço", 3604: "Serviço", 3605: "Serviço",
        3606: "Serviço", 3607: "Serviço", 3608: "Serviço", 3609: "Serviço", 3610: "Serviço",
        3612: "Serviço", 3613: "Serviço", 3614: "Serviço", 3615: "Serviço", 3616: "Serviço",
        3617: "Serviço", 3618: "Serviço", 3619: "Serviço", 3620: "Serviço", 3621: "Serviço",
        3622: "Serviço", 3623: "Serviço", 3624: "Serviço", 3625: "Serviço", 3626: "Serviço",
        3627: "Serviço", 3628: "Serviço", 3629: "Serviço", 3630: "Serviço", 3631: "Serviço",
        3632: "Serviço", 3633: "Serviço", 3699: "Serviço",
        3701: "Serviço", 3702: "Serviço", 3703: "Serviço", 3704: "Serviço", 3705: "Serviço",
        3706: "Serviço", 3707: "Serviço",
        3901: "Serviço", 3902: "Serviço", 3903: "Serviço", 3904: "Serviço", 3905: "Serviço",
        3906: "Serviço", 3907: "Serviço", 3908: "Serviço", 3909: "Serviço", 3910: "Serviço",
        3911: "Serviço", 3912: "Serviço", 3913: "Serviço", 3914: "Serviço", 3915: "Serviço",
        3918: "Serviço", 3921: "Serviço", 3922: "Serviço", 3923: "Serviço", 3924: "Serviço",
        3925: "Serviço", 3926: "Serviço", 3927: "Serviço", 3928: "Serviço", 3929: "Serviço",
        3930: "Serviço", 3931: "Serviço", 3932: "Serviço", 3933: "Serviço", 3934: "Serviço",
        3935: "Serviço", 3936: "Serviço", 3937: "Serviço", 3938: "Serviço", 3939: "Serviço",
        3940: "Serviço", 3941: "Serviço", 3942: "Serviço", 3943: "Serviço", 3944: "Serviço",
        3945: "Serviço", 3946: "Serviço", 3947: "Serviço", 3948: "Serviço", 3949: "Serviço",
        3950: "Serviço", 3951: "Serviço", 3952: "Serviço", 3953: "Serviço", 3954: "Serviço",
        3955: "Serviço", 3956: "Serviço", 3957: "Serviço", 3958: "Serviço", 3959: "Serviço",
        3960: "Serviço", 3961: "Serviço", 3962: "Serviço", 3963: "Serviço", 3964: "Serviço",
        3965: "Serviço", 3966: "Serviço", 3967: "Serviço", 3968: "Serviço", 3969: "Serviço",
        3970: "Serviço", 3971: "Serviço", 3972: "Serviço", 3973: "Serviço", 3974: "Serviço",
        3975: "Serviço", 3976: "Serviço", 3977: "Serviço", 3978: "Serviço", 3979: "Serviço",
        3980: "Serviço", 3981: "Serviço", 3982: "Serviço", 3983: "Serviço", 3984: "Serviço",
        3985: "Serviço", 3986: "Serviço", 3987: "Serviço", 3988: "Serviço", 3989: "Serviço",
        3990: "Serviço", 3991: "Serviço", 3992: "Serviço", 3993: "Serviço", 3994: "Serviço",
        3995: "Serviço", 3996: "Serviço", 3997: "Serviço", 3998: "Serviço", 3999: "Serviço",
        4001: "Serviço", 4002: "Serviço", 4003: "Serviço", 4004: "Serviço", 4005: "Serviço",
        4006: "Serviço", 4007: "Serviço",

        # Locação
        3611: "Locação", 3916: "Locação", 3917: "Locação",
        3919: "Locação", 3920: "Locação",

        # Obras
        5100: "Obras", 5102: "Obras", 5103: "Obras", 5104: "Obras",
        5105: "Obras", 5106: "Obras", 5107: "Obras", 5108: "Obras",
        5109: "Obras", 5110: "Obras", 5111: "Obras", 5112: "Obras",
        5113: "Obras", 5114: "Obras", 5115: "Obras", 5116: "Obras"
    }


    df["Tipo"] = df["Elemento Item Despesa - Código"].map(tipo_map)
    return df

