const Discord = require('discord.js');
 const client = new Discord.Client();

client.on('ready', () => {
 console.log(`Logged in as ${client.user.tag}!`);
 });

client.on('message', msg => {
 if (msg.content === '@splenda') {
 msg.reply('<@385933420389335061>');
 }
 if (msg.content === ':(') {
 msg.reply('cheer up. theres no need to be sad. the world is a wonderful place. i mean, it kinda sucks here. but its as wonderful as you make it. so make it wonderful');
 }
if (msg.content === 'D:') {
 msg.reply('shocking');
 }
if (msg.content === 'XD') {
 msg.reply('lulz');
 } 
if (msg.content === 'bitch') {
 msg.channel.send('lasagna');
 } 

if (msg.content === ':))))') {
 msg.reply('Woah, calm yo tits there. no one has that many chins');
 } 
 });

client.login('NTYwNDQ2Mjk5MDQwNjQ1MTIy.D30D6Q.hNV_vjd1UQdwdaA_xTXhc3NaD1w');
