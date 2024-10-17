func potenciaModulada(a: Int, b: Int, c: Int) -> Int {
    guard c >= 2 else {
        fatalError("El valor de c debe ser mayor o igual a 2.")
    }
    
    if b == 0 {
        return 1
    }
    
    let aModC = a % c
    let potenciaMenosUno = potenciaModulada(a: aModC, b: b - 1, c: c)
    
    return (aModC * potenciaMenosUno) % c
}

// Ejemplo de uso
let a = 12 // 12 12 12
let b = 1  // 2  3  4
let c = 5  // 5  5  5

let resultado = potenciaModulada(a: a, b: b, c: c)
print("El resultado de \(a)^\(b) mod \(c) es: \(resultado)") // 2 4 3 1
