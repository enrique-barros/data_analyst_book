# Ejercicios SQL - Tabla Customers

Este conjunto de ejercicios está diseñado para practicar los conceptos básicos de SQL utilizando la tabla `customers`. Todos los ejercicios se pueden resolver con los conocimientos adquiridos en la unidad.

---

## Estructura de la tabla `customers`

La tabla `customers` contiene la siguiente información de clientes:

| Columna | Descripción |
|---------|-------------|
| `customerNumber` | Identificador único del cliente |
| `customerName` | Nombre de la empresa del cliente |
| `contactLastName` | Apellido del contacto principal |
| `contactFirstName` | Nombre del contacto principal |
| `phone` | Teléfono de contacto |
| `addressLine1` | Primera línea de dirección |
| `addressLine2` | Segunda línea de dirección |
| `city` | Ciudad |
| `state` | Estado/Provincia |
| `postalCode` | Código postal |
| `country` | País |
| `salesRepEmployeeNumber` | Número de empleado del representante de ventas |
| `creditLimit` | Límite de crédito |

---

## Ejercicio 1: Obtener todas las columnas

**Enunciado:**
Escribe una consulta SQL que muestre TODOS los datos de la tabla `customers`.

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT * FROM customers;
```

**Explicación:**
El asterisco `*` es un comodín que representa todas las columnas de la tabla. La cláusula `FROM` indica de dónde obtener los datos.

</details>

---

## Ejercicio 2: Obtener columnas específicas

**Enunciado:**
Escribe una consulta SQL que muestre solamente el nombre del cliente (`customerName`), el teléfono (`phone`) y el país (`country`).

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT customerName, phone, country FROM customers;
```

**Explicación:**
Especificamos las columnas que deseamos entre `SELECT` y `FROM`, separadas por comas. El orden en que las escribimos es el orden en que aparecerán en el resultado.

</details>

---

## Ejercicio 3: Usar alias en una columna

**Enunciado:**
Escribe una consulta que muestre el `customerNumber` con el alias "ID Cliente" y `customerName` con el alias "Nombre Empresa".

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT customerNumber AS "ID Cliente", customerName AS "Nombre Empresa" FROM customers;
```

**Explicación:**
Utilizamos la palabra clave `AS` para crear un alias (nombre alternativo) para cada columna. Si el alias contiene espacios, debe ir entre comillas dobles. Los alias aparecerán como encabezados de columna en el resultado.

</details>

---

## Ejercicio 4: Alias sin AS

**Enunciado:**
Escribe una consulta que muestre `contactFirstName` con el alias "Nombre" y `contactLastName` con el alias "Apellido". Usa la sintaxis sin `AS`.

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT contactFirstName "Nombre", contactLastName "Apellido" FROM customers;
```

**Explicación:**
En SQL, es posible escribir el alias directamente después del nombre de la columna sin usar `AS`. Ambas formas son válidas.

</details>

---

## Ejercicio 5: Mostrar datos de contacto

**Enunciado:**
Escribe una consulta que muestre el nombre de la empresa (`customerName`), el nombre completo del contacto (combinando `contactFirstName` y `contactLastName`) con alias "Contacto", y el teléfono (`phone`).

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT customerName, contactFirstName, contactLastName AS "Contacto", phone FROM customers;
```

**Explicación:**
Si deseamos combinar texto de dos columnas, necesitaríamos usar una función de concatenación, que está fuera del alcance de estos ejercicios iniciales. Por ahora, mostramos las columnas por separado o podemos mencionarlas en el orden deseado.

</details>

---

## Ejercicio 6: Información de dirección

**Enunciado:**
Crea una consulta que muestre la información de dirección de los clientes: nombre de cliente (`customerName`), ciudad (`city`), estado (`state`) y país (`country`).

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT customerName, city, state, country FROM customers;
```

**Explicación:**
Seleccionamos las columnas relacionadas con la ubicación del cliente. El orden de las columnas en la cláusula `SELECT` es importante y determinará cómo se presentan los datos.

</details>

---

## Ejercicio 7: Límite de crédito

**Enunciado:**
Escribe una consulta que muestre el nombre del cliente (`customerName`) con el alias "Cliente" y el límite de crédito (`creditLimit`) con el alias "Crédito Máximo".

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT customerName AS "Cliente", creditLimit AS "Crédito Máximo" FROM customers;
```

**Explicación:**
Los alias hacen que los resultados sean más legibles, especialmente cuando los nombres originales de las columnas no son tan claros para el usuario final.

</details>

---

## Ejercicio 8: Datos del representante de ventas

**Enunciado:**
Escribe una consulta que muestre el número de cliente (`customerNumber`), el nombre del cliente (`customerName`) y el número del representante de ventas asignado (`salesRepEmployeeNumber`).

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT customerNumber, customerName, salesRepEmployeeNumber FROM customers;
```

**Explicación:**
Esta consulta obtiene información sobre la relación entre clientes y sus representantes de ventas, sin aplicar filtros ni condiciones.

</details>

---

## Ejercicio 9: Alias con espacios

**Enunciado:**
Crea una consulta que muestre `phone` con el alias "Número de Teléfono" y `addressLine1` con el alias "Dirección Principal".

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT phone AS "Número de Teléfono", addressLine1 AS "Dirección Principal" FROM customers;
```

**Explicación:**
Cuando un alias contiene espacios u otros caracteres especiales, debe incluirse entre comillas dobles. Sin las comillas, SQL interpretaría cada palabra como un alias separado, causando un error de sintaxis.

</details>

---

## Ejercicio 10: Información de contacto completa

**Enunciado:**
Escribe una consulta que muestre:
- `customerNumber` con alias "Código Cliente"
- `customerName` con alias "Empresa"
- `contactFirstName` con alias "Nombre Contacto"
- `contactLastName` con alias "Apellido Contacto"
- `phone` con alias "Teléfono"

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT 
  customerNumber AS "Código Cliente",
  customerName AS "Empresa",
  contactFirstName AS "Nombre Contacto",
  contactLastName AS "Apellido Contacto",
  phone AS "Teléfono"
FROM customers;
```

**Explicación:**
Aunque el formato se extiende por varias líneas (lo que es recomendable para la legibilidad), la consulta funciona exactamente igual. SQL ignora los saltos de línea y espacios en blanco. Este formato hace que la consulta sea más fácil de leer y mantener.

</details>

---

## Ejercicio 11: Práctica de orden de columnas

**Enunciado:**
Escribe dos consultas diferentes que muestren `phone`, `customerName` y `country`:
1. Primera versión: en el orden original (phone, customerName, country)
2. Segunda versión: en orden alfabético de columnas (country, customerName, phone)

<details>
<summary><b>Ver solución</b></summary>

**Solución - Primera versión:**
```sql
SELECT phone, customerName, country FROM customers;
```

**Solución - Segunda versión:**
```sql
SELECT country, customerName, phone FROM customers;
```

**Explicación:**
El orden en que especificamos las columnas en la cláusula `SELECT` determina el orden en que aparecerán en los resultados. Las mismas columnas en diferente orden producen resultados con una presentación distinta.

</details>

---

## Ejercicio 12: Datos mínimos de cliente

**Enunciado:**
Crea una consulta que muestre solo 4 columnas de la tabla customers:
- El identificador del cliente
- El nombre de la empresa
- La ciudad
- El país

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT customerNumber, customerName, city, country FROM customers;
```

**Explicación:**
Esta es una consulta simple que selecciona columnas específicas sin ningún filtro. Es útil cuando necesitamos una visión general de los clientes sin demasiados detalles.

</details>

---

## Ejercicio 13: Información fiscal y contacto

**Enunciado:**
Escribe una consulta que muestre `customerName` con alias "Razón Social", `contactFirstName` y `contactLastName`, y `creditLimit` con alias "Límite Crédito".

<details>
<summary><b>Ver solución</b></summary>

**Solución:**
```sql
SELECT 
  customerName AS "Razón Social",
  contactFirstName,
  contactLastName,
  creditLimit AS "Límite Crédito"
FROM customers;
```

**Explicación:**
Combinamos columnas con y sin alias. Los alias ayudan a clarificar términos técnicos (como `creditLimit`) en términos más comerciales (como "Límite Crédito").

</details>

---

## Ejercicio 14: Columnas sin alias repetidas

**Enunciado:**
¿Cuál es el resultado de ejecutar la siguiente consulta?

```sql
SELECT customerName, customerName, city FROM customers;
```

<details>
<summary><b>Ver solución</b></summary>

**Respuesta:**
La consulta es válida y mostraría la columna `customerName` dos veces, seguida de la columna `city`. Aunque no es práctica común, SQL no impide seleccionar la misma columna múltiples veces.

**Resultado esperado:**
Tres columnas: customerName, customerName (repetida), city.

</details>

---

## Ejercicio 15: Orden de escritura en SQL

**Enunciado:**
Identifica el orden correcto en el que SQL debe interpretar una consulta básica. Ordena estas cláusulas:

1. `FROM customers`
2. `SELECT customerName, phone`

<details>
<summary><b>Ver solución</b></summary>

**Respuesta:**
Aunque escribimos `SELECT` primero en el código, SQL procesa la consulta en este orden:

1. `FROM customers` - Primero, identifica la tabla
2. `SELECT customerName, phone` - Luego, selecciona las columnas

Orden de escritura (en el código):
```sql
SELECT customerName, phone FROM customers;
```

Orden de ejecución (como SQL lo procesa):
1. FROM (ubicar tabla)
2. SELECT (elegir columnas)

**Explicación:**
Entender la diferencia entre el orden de escritura (sintaxis) y el orden de ejecución (semántica) es importante para comprender cómo funciona SQL internamente.

</details>

---

## Consejos para evitar errores comunes

### Error 1: Olvidar comillas en alias con espacios
❌ **Incorrecto:**
```sql
SELECT customerName AS Nombre Empresa FROM customers;
```

✅ **Correcto:**
```sql
SELECT customerName AS "Nombre Empresa" FROM customers;
```

### Error 2: Escribir el alias antes del nombre de columna
❌ **Incorrecto:**
```sql
SELECT "Mi Alias" customerName FROM customers;
```

✅ **Correcto:**
```sql
SELECT customerName AS "Mi Alias" FROM customers;
```

### Error 3: Olvidar FROM
❌ **Incorrecto:**
```sql
SELECT customerName, phone;
```

✅ **Correcto:**
```sql
SELECT customerName, phone FROM customers;
```

### Error 4: Mayúsculas/minúsculas en nombres de columnas
Nota: Los nombres de columnas en SQL generalmente no distinguen entre mayúsculas y minúsculas, pero es buena práctica respetar la estructura de la tabla.

```sql
SELECT CUSTOMERNAME FROM customers;  -- Generalmente funciona
SELECT customerName FROM customers;  -- Forma correcta
```

---

## Resumen de conceptos

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| **SELECT** | Especifica qué columnas mostrar | `SELECT customerName, phone` |
| **\*** | Comodín para todas las columnas | `SELECT * FROM customers` |
| **FROM** | Especifica de dónde obtener datos | `FROM customers` |
| **AS** | Crea un alias para una columna | `customerName AS "Nombre"` |
| **Alias sin AS** | Alias directo sin la palabra clave | `customerName "Nombre"` |
| **Orden de columnas** | El orden en SELECT determina el orden de visualización | Importante para la presentación |

---

## ¿Necesitas más ayuda?

Si tienes dudas sobre algún ejercicio o necesitas más práctica, recuerda:
- Revisa la anatomía de una consulta básica
- Practica escribiendo consultas simples con SELECT y FROM
- Experimenta con diferentes órdenes de columnas
- Usa alias para hacer tus resultados más claros
