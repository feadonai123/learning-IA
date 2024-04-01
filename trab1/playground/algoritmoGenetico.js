// Daniel Shiffman
// The Coding Train
// Traveling Salesperson with Genetic Algorithm

// https://thecodingtrain.com/CodingChallenges/035.4-tsp.html
// https://youtu.be/M3KTWnTrU_c
// https://thecodingtrain.com/CodingChallenges/035.5-tsp.html
// https://youtu.be/hnxn6DtLYcY

function swap(a, i, j) {
  const temp = a[i];
  a[i] = a[j];
  a[j] = temp;
}

function dist(x1, y1, x2, y2) {
  return Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2);
}

function calcDistance(points, order) {
  let sum = 0;
  for (let i = 0; i < order.length - 1; i++) {
    const cityAIndex = order[i];
    const cityA = points[cityAIndex];
    const cityBIndex = order[i + 1];
    const cityB = points[cityBIndex];
    const d = dist(cityA.x, cityA.y, cityB.x, cityB.y);
    sum += d;
  }
  return sum;
}

function calculateFitness() {
  let currentRecord = Infinity;
  for (let i = 0; i < population.length; i++) {
    const d = calcDistance(cities, population[i]);
    if (d < recordDistance) {
      recordDistance = d;
      bestEver = population[i];
    }
    if (d < currentRecord) {
      currentRecord = d;
      currentBest = population[i];
    }

    // This fitness function has been edited from the original video
    // to improve performance, as discussed in The Nature of Code 9.6 video,
    // available here: https://www.youtube.com/watch?v=HzaLIO9dLbA
    fitness[i] = 1 / (Math.pow(d, 8) + 1);
  }
}

function normalizeFitness() {
  let sum = 0;
  for (let i = 0; i < fitness.length; i++) {
    sum += fitness[i];
  }
  for (let i = 0; i < fitness.length; i++) {
    fitness[i] = fitness[i] / sum;
  }
}

function nextGeneration() {
  const newPopulation = [];
  for (var i = 0; i < population.length; i++) {
    const orderA = pickOne(population, fitness);
    const orderB = pickOne(population, fitness);
    const order = crossOver(orderA, orderB);
    mutate(order, 0.1);
    newPopulation[i] = order;
  }
  population = newPopulation;
}

function pickOne(list, prob) {
  let index = 0;
  let r = Math.random(1);

  while (r > 0) {
    r = r - prob[index];
    index++;
  }
  index--;
  return list[index].slice();
}

function crossOver(orderA, orderB) {
  const start = Math.floor(Math.random(orderA.length));
  const end = Math.floor(Math.random(start + 1, orderA.length));
  const neworder = orderA.slice(start, end);
  // var left = totalCities - neworder.length;
  for (let i = 0; i < orderB.length; i++) {
    const city = orderB[i];
    if (!neworder.includes(city)) {
      neworder.push(city);
    }
  }
  return neworder;
}


function mutate(order, mutationRate) {
  for (let i = 0; i < totalCities; i++) {
    if (Math.random(1) < mutationRate) {
      const indexA = Math.floor(Math.random(order.length));
      const indexB = (indexA + 1) % totalCities;
      swap(order, indexA, indexB);
    }
  }
}


function algortimoGenetico(qtdGeracoes){
  for (let i = 0; i < qtdGeracoes; i++) {
    console.log('\nGeração: ', i)
    for (let j = 0; j < population.length; j++) {
      console.log(population[j].join(' ,'), 'Distância: ', calcDistance(cities, population[j]))
    }
    calculateFitness();
    normalizeFitness();
    nextGeneration();
  }

  console.log('\nMelhor caminho: ', bestEver, 'Distância: ', recordDistance)
}

let population = [[2, 4, 8, 3, 9, 0, 5, 7, 1, 6], [7, 3, 4, 0, 8, 5, 2, 9, 6, 1], [5, 3, 9, 8, 7, 2, 6, 4, 0, 1], [0, 1, 6, 9, 8, 5, 2, 7, 3, 4], [8, 7, 4, 9, 1, 6, 3, 2, 5, 0], [9, 3, 5, 0, 6, 2, 1, 7, 8, 4], [5, 8, 6, 9, 1, 7, 0, 3, 2, 4], [7, 8, 0, 1, 2, 5, 6, 3, 4, 9], [3, 4, 8, 5, 6, 0, 9, 1, 7, 2], [3, 0, 8, 4, 1, 6, 2, 7, 5, 9]]
const cities = [
  {
    x: 82,
    y: 3
  }, {
    x: 88,
    y: 16
  }, {
    x: 29,
    y: 55
  }, {
    x: 84,
    y: 86
  }, {
    x: 57,
    y: 29
  }, {
    x: 10,
    y: 85
  }, {
    x: 35,
    y: 30
  }, {
    x: 54,
    y: 10
  }, {
    x: 80,
    y: 52
  }, {
    x: 78,
    y: 60
  }
]
const totalCities = 10;
const popSize = 10;

const fitness = [];

let recordDistance = Infinity;
let bestEver;
let currentBest;

algortimoGenetico(1000);