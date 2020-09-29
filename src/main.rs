use std::env;

//use serenity::{
//    async_trait,
//    model::{channel::Message, gateway::Ready},
//    prelude::*,
//};
use serenity::{
    async_trait,
    client::bridge::gateway::{GatewayIntents, ShardManager},
//    framework::standard::{macros::group, StandardFramework},
    http::Http,
    model::{
        channel::Message,
        event::MessageUpdateEvent,
        gateway::Ready,
        guild::{Member, Role},
        id::{ChannelId, GuildId, MessageId, RoleId},
        user::User,
    },
    prelude::*,
};

struct Handler;

#[async_trait]
impl EventHandler for Handler {
    // Set a handler for the `message` event - so that whenever a new message
    // is received - the closure (or function) passed will be called.
    //
    // Event handlers are dispatched through a threadpool, and so multiple
    // events can be dispatched simultaneously.
    async fn message(&self, ctx: Context, msg: Message) {
        if msg.author.bot {
            return;
        }

        if msg.content == "bitch" {
            // Sending a message can fail, due to a network error, an
            // authentication error, or lack of permissions to post in the
            // channel, so log to stdout when some error happens, with a
            // description of it.
            if let Err(why) = msg.channel_id.say(&ctx.http, "LASAGNA!!!").await {
                println!("Error sending message: {:?}", why);
            }

        }

        if msg.content.starts_with("I'm") {
            //if let Err(why) = msg.channel_id.say(&ctx.http, msg.content).await {
            let copied = msg.content.replace("I'm", "");
            if let Err(why) = msg.channel_id.say(&ctx.http, ("Hi".to_owned() + &copied + ", I'm dad.")).await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.contains("uwu") {
            //if let Err(why) = msg.channel_id.say(&ctx.http, msg.content).await {
            if let Err(why) = msg.channel_id.say(&ctx.http, "OwO").await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.contains("oof") {
            //if let Err(why) = msg.channel_id.say(&ctx.http, msg.content).await {
            if let Err(why) = msg.channel_id.say(&ctx.http, "no").await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.contains("mallcop") {
            //if let Err(why) = msg.channel_id.say(&ctx.http, msg.content).await {
            if let Err(why) = msg.channel_id.say(&ctx.http, "A mustache a day keeps the shoplifters at bay").await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.to_lowercase().contains("nooo") {
            //if let Err(why) = msg.channel_id.say(&ctx.http, msg.content).await {
            if let Err(why) = msg.channel_id.say(&ctx.http, "https://tenor.com/view/no-theoffice-stevecarrell-michaelscott-gif-4652931").await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.to_lowercase().contains("bad bot") {
            //if let Err(why) = msg.channel_id.say(&ctx.http, msg.content).await {
            if let Err(why) = msg.channel_id.say(&ctx.http, "you're not my dad").await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.to_lowercase().contains("peter") {
            //if let Err(why) = msg.channel_id.say(&ctx.http, msg.content).await {
            if let Err(why) = msg.channel_id.say(&ctx.http, "feature coming soon").await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.to_lowercase().contains(":(") {
            //if let Err(why) = msg.channel_id.say(&ctx.http, msg.content).await {
            if let Err(why) = msg.channel_id.say(&ctx.http, "https://tenor.com/view/30rock-alec-baldwin-there-there-cheer-up-comfort-gif-4215371").await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.starts_with("D:") {
            if let Err(why) = msg.channel_id.say(&ctx.http, "shocking").await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.starts_with("XD") {
            if let Err(why) = msg.channel_id.say(&ctx.http, "lulz").await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.to_lowercase() == "f" {
            if let Err(why) = msg.channel_id.say(&ctx.http, "salute to the fallen https://tenor.com/view/press-f-pay-respect-keyboard-gif-12855017").await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.contains("@splenda") {
            if let Err(why) = msg.channel_id.say(&ctx.http, (msg.author.to_string() + " mentioned you, splenda. <@385933420389335061>")).await {
                println!("Error sending message: {:?}", why);
            }
        }
        if msg.content.contains("wow") {
            if let Err(why) = msg.channel_id.say(&ctx.http, "https://tenor.com/view/owen-wilson-wow-snapchat-gif-12686549").await {
                println!("Error sending message: {:?}", why);
            }
        }


    }

    async fn guild_member_addition(&self, ctx: Context, guild_id: GuildId, new_member: Member) {
        let channel_id = ChannelId::from(510553881764298766 as u64);
        if let Err(why) = channel_id.say(&ctx.http, ("hey look, its a ".to_owned() + &new_member.user.mention())).await {
            println!("Error sending message: {:?}", why);
        }
    }

    async fn guild_member_removal(&self, ctx: Context, guild_id: GuildId, user: User) {
        let channel_id = ChannelId::from(510553881764298766 as u64);
        if let Err(why) = channel_id.say(&ctx.http, ("goodbye ".to_owned() + &user.name)).await {
            println!("Error sending message: {:?}", why);
        }
    }



    // Set a handler to be called on the `ready` event. This is called when a
    // shard is booted, and a READY payload is sent by Discord. This payload
    // contains data like the current user's guild Ids, current user data,
    // private channels, and more.
    //
    // In this case, just print what the current user's username is.
    async fn ready(&self, ctx: Context, ready: Ready) {
        println!("{} is connected!", ready.user.name);
        use serenity::model::gateway::Activity;
        use serenity::model::user::OnlineStatus;

        let game = Activity::playing("Minecraft, but for bots");
        let status = OnlineStatus::Idle;

        ctx.set_presence(Some(game), status).await;
    }
}

#[tokio::main]
async fn main() {
    // Configure the client with your Discord bot token in the environment.
    let token = env::var("DISCORD_TOKEN")
        .expect("Expected a token in the environment");

    // Create a new instance of the Client, logging in as a bot. This will
    // automatically prepend your bot token with "Bot ", which is a requirement
    // by Discord for bot users.
    let mut client = Client::new(&token)
        .event_handler(Handler)
        .await
        .expect("Err creating client");

    // Finally, start a single shard, and start listening to events.
    //
    // Shards will automatically attempt to reconnect, and will perform
    // exponential backoff until it reconnects.
    if let Err(why) = client.start().await {
        println!("Client error: {:?}", why);
    }
}
