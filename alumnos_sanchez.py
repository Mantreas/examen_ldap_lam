def create_students_ldif(filename, class_name, num_students, base_dn):
    """Genera un archivo LDIF con alumnos asociados a una clase."""
    
    try:
        with open(filename, "w") as f:
            for i in range(1, num_students + 1):
                student_name = f"Alumno{i}"  # Asignamos un nombre genérico a cada alumno
                student_dn = f"uid={student_name},{base_dn}"  # Distinguished Name para cada alumno
                ldif_content = f"""# student record for {student_name} in class {class_name}
dn: {student_dn}
changetype: add
objectClass: inetOrgPerson
uid: {student_name}
cn: {student_name}
sn: {student_name}
mail: {student_name}@example.com
ou: {class_name}

"""
                f.write(ldif_content)
        
        print(f"LDIF file '{filename}' created successfully.")
    
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Parámetros de entrada
class_name = "1ESOC"  # Nombre de la clase
num_students = 20     # Número de alumnos
base_dn = "dc=sanchez,dc=org"  # Tu DN base

# Llamada a la función para generar el archivo LDIF
filename = "alumnos_sanchez.ldif"
create_students_ldif(filename, class_name, num_students, base_dn)
