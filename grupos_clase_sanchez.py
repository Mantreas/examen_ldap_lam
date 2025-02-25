def create_organizational_units_ldif(filename, ou_list, base_dn):
    """Creates an LDIF file for multiple organizational units from a list."""

    try:
        with open(filename, "w") as f:
            for ou_name in ou_list:
                ldif_content = f"""# organisational unit for {ou_name} department
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}

"""
                f.write(ldif_content)
        
        print(f"LDIF file '{filename}' created successfully.")
    
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Lista de unidades organizacionales
ou_list = ["1ESOA", "1ESOB", "1ESOC", "1ESOD"]  # Lista de grupos de clase
base_dn = "dc=sanchez,dc=org"  # Tu DN base

# Llamada a la función para crear el archivo LDIF
filename = "ou_sanchez.ldif"
create_organizational_units_ldif(filename, ou_list, base_dn)
