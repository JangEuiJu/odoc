const [[N], [X, Y, R], ...T] = require('fs')
	.readFileSync('./dev/stdin')
	.toString()
	.trim()
	.split('\n')
	.map((v) => v.split(' ').map(Number));

const left = X - R;
const right = X + R;

let A = 0;
let B = 0;

T.forEach(([v]) => {
	if (v == left || v == right) {
		B++;
	} else if (v > left && v < right) {
		A++;
	}
});

console.log(A, B);