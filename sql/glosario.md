# Glosario: SQL Básico con SELECT

| Término | Definición |
|---------|-----------|
| **Base de Datos** | Conjunto organizado de datos almacenados de manera estructurada para facilitar su acceso y análisis. |
| **Tabla** | Estructura que organiza datos en filas y columnas, similar a una hoja de cálculo. |
| **Fila (Row)** | Registro individual que contiene información de una entidad específica en una tabla. |
| **Columna (Column)** | Atributo o campo que representa una característica específica de los datos. |
| **Campo** | Unidad individual de información que forma parte de un registro o fila. |
| **Tipos de Datos** | Categoría que define qué tipo de información puede almacenarse en un campo (números, texto, fechas). |
| **Consulta (Query)** | Instrucción SQL que solicita información específica de una base de datos. |
| **SELECT** | Comando SQL que recupera datos específicos de una o más tablas. |
| **FROM** | Cláusula que especifica de cuál tabla o tablas se extraerán los datos. |
| **Anatomía de una Consulta** | Estructura básica de una consulta SQL con sus componentes principales (SELECT, FROM, WHERE, etc.). |
| **Alias de Columnas** | Nombre alternativo temporal asignado a una columna en los resultados de una consulta. |
| **AS** | Palabra clave usada para crear alias para columnas. |
| **Orden de Escritura SQL** | Secuencia en que se escriben las cláusulas de una consulta SQL para que sea correcta. |
| **WHERE** | Cláusula que filtra resultados aplicando condiciones específicas a los datos. |
| **Filtrado** | Proceso de seleccionar solo las filas que cumplen criterios específicos. |
| **Operador Lógico AND** | Operador que requiere que todas las condiciones sean verdaderas. |
| **Operador Lógico OR** | Operador que requiere que al menos una de las condiciones sea verdadera. |
| **Operador Lógico NOT** | Operador que niega o invierte una condición. |
| **Operador IN** | Operador que verifica si un valor coincide con cualquier valor en una lista. |
| **Operador LIKE** | Operador que busca patrones en valores de texto. |
| **Operador BETWEEN** | Operador que filtra valores dentro de un rango específico. |
| **Operadores de Comparación** | Símbolos utilizados para comparar valores (=, <>, <, >, <=, >=). |
| **Rangos** | Intervalo de valores definido para filtrar datos entre un mínimo y máximo. |
| **Problemas con los Datos** | Inconsistencias o errores en los datos que afectan los resultados de las consultas. |
| **Negación de Condiciones** | Uso de NOT para invertir el resultado de una condición de búsqueda. |
| **ORDER BY** | Cláusula que ordena los resultados de una consulta en orden ascendente o descendente. |
| **ASC** | Abreviatura de ascendente; ordena datos de menor a mayor o alfabéticamente (A-Z). |
| **DESC** | Abreviatura de descendente; ordena datos de mayor a menor o alfabéticamente inverso (Z-A). |
| **Ordenamiento** | Proceso de arreglar los resultados en un orden específico. |
| **Orden Alfanumérico** | Ordenamiento basado en caracteres alfabéticos y numéricos. |
| **Ordenar Varias Columnas** | Aplicar orden a múltiples columnas dentro de la misma consulta. |
| **Ordenamientos Diferentes** | Usar diferentes direcciones de orden (ASC o DESC) para diferentes columnas. |
| **Ordenamientos con Filtro** | Combinar cláusulas WHERE y ORDER BY para filtrar y ordenar simultáneamente. |
| **Función COUNT** | Función de agregación que cuenta el número de filas o valores. |
| **Función SUM** | Función de agregación que suma valores numéricos de una columna. |
| **Función AVG** | Función de agregación que calcula el promedio de valores numéricos. |
| **Función MAX** | Función de agregación que devuelve el valor máximo de una columna. |
| **Función MIN** | Función de agregación que devuelve el valor mínimo de una columna. |
| **Funciones de Agregado** | Funciones que combinan múltiples filas y devuelven un resultado único. |
| **Agregación** | Proceso de combinar múltiples filas en un resultado único usando funciones. |
| **Funciones Escalares** | Funciones que operan sobre valores individuales devolviendo un resultado por cada fila. |
| **Operaciones Aritméticas** | Cálculos matemáticos básicos (suma, resta, multiplicación, división) dentro de consultas. |
| **Función ROUND** | Función que redondea un número a un número específico de decimales. |
| **Función CEIL** | Función que redondea hacia arriba al número entero más cercano. |
| **Función FLOOR** | Función que redondea hacia abajo al número entero más cercano. |
| **Función ABS** | Función que devuelve el valor absoluto (positivo) de un número. |
| **Función MOD** | Función que devuelve el residuo de una división. |
| **Funciones Numéricas** | Funciones que realizan operaciones matemáticas sobre valores numéricos. |
| **Función UPPER** | Función que convierte texto a mayúsculas. |
| **Función LOWER** | Función que convierte texto a minúsculas. |
| **Función TRIM** | Función que elimina espacios en blanco al inicio y final de una cadena de texto. |
| **Función SUBSTRING** | Función que extrae una parte de una cadena de texto. |
| **Funciones de Texto** | Funciones que manipulan y transforman valores de texto. |
| **Función COALESCE** | Función que devuelve el primer valor no nulo de una lista de valores. |
| **Control de Nulos** | Técnicas para manejar valores NULL (ausencia de datos) en consultas. |
| **NULL** | Valor que representa la ausencia de datos o información desconocida. |
| **IS NULL** | Condición que verifica si un valor es nulo o está vacío. |
| **IS NOT NULL** | Condición que verifica si un valor no es nulo. |
| **CASE** | Estructura condicional que devuelve diferentes valores según condiciones específicas. |
| **CASE WHEN** | Estructura condicional con una o más condiciones y sus resultados correspondientes. |
| **Condicionales** | Estructuras de control que ejecutan diferentes acciones según se cumplan condiciones. |
| **GROUP BY** | Cláusula que agrupa filas con valores idénticos en columnas especificadas. |
| **Agrupación de Datos** | Proceso de organizar resultados en grupos basados en valores similares. |
| **HAVING** | Cláusula que filtra grupos creados por GROUP BY según condiciones. |
| **Cardinalidades** | Número de registros en la relación entre tablas. |
| **Relación Uno a Muchos (1..n)** | Tipo de relación donde un registro en una tabla se asocia con múltiples registros en otra. |
| **Relación Uno a Uno (1..1)** | Tipo de relación donde un registro en una tabla se asocia con exactamente un registro en otra. |
| **Relación Cero a Uno (0..1)** | Tipo de relación donde un registro en una tabla puede no asociarse o asociarse a un registro en otra. |
| **Tabla Izquierda** | Primera tabla mencionada en una operación JOIN. |
| **Tabla Derecha** | Segunda tabla mencionada en una operación JOIN. |
| **JOIN** | Operación que combina datos de dos o más tablas basándose en una condición común. |
| **INNER JOIN** | Devuelve solo las filas que coinciden en ambas tablas. |
| **LEFT JOIN** | Devuelve todas las filas de la tabla izquierda más las coincidencias de la derecha. |
| **Uniones** | Operaciones que combinan datos de múltiples tablas. |
| **Subconsulta** | Consulta dentro de otra consulta que devuelve datos usados por la consulta principal. |
| **Errores de Sintaxis** | Errores causados por no seguir correctamente las reglas del lenguaje SQL. |
| **Errores Semánticos** | Errores donde la sintaxis es correcta pero la consulta no hace lo que se intenta. |
| **Hoja de Datos** | Vista de resultados de una consulta mostrada en formato de tabla. |
| **Escritura SQL** | Práctica de escribir código SQL correctamente y de manera legible. |
