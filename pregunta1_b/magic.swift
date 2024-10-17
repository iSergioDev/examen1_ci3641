func esMatrizMagica(matriz: [[Int]]) -> Bool {
    let n = matriz.count // Dimensión de la matriz (N x N)
    
    // Verificamos si la matriz es cuadrada
    guard n > 0 && matriz.allSatisfy({ $0.count == n }) else {
        return false
    }
    
    // Suma de la primera fila como el objetivo
    let sumaMagica = matriz[0].reduce(0, +)
    
    // Verificar sumas de filas
    for fila in matriz {
        if fila.reduce(0, +) != sumaMagica {
            return false
        }
    }
    
    // Verificar sumas de columnas
    for col in 0..<n {
        var sumaColumna = 0
        for fila in 0..<n {
            sumaColumna += matriz[fila][col]
        }
        if sumaColumna != sumaMagica {
            return false
        }
    }
    
    // Verificar suma de la diagonal principal
    var sumaDiagonalPrincipal = 0
    for i in 0..<n {
        sumaDiagonalPrincipal += matriz[i][i]
    }
    if sumaDiagonalPrincipal != sumaMagica {
        return false
    }
    
    // Verificar suma de la diagonal secundaria
    var sumaDiagonalSecundaria = 0
    for i in 0..<n {
        sumaDiagonalSecundaria += matriz[i][n - 1 - i]
    }
    if sumaDiagonalSecundaria != sumaMagica {
        return false
    }
    
    // Si todas las condiciones se cumplen, es una matriz mágica
    return true
}

// Ejemplo de uso
let matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

if esMatrizMagica(matriz: matriz) {
    print("La matriz es mágica.")
} else {
    print("La matriz no es mágica.")
}
