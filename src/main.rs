use std::env;
use tokio;
//use serenity::model::channel::AttachmentType;
use serenity::{
    async_trait,
//    http::Http,
    model::{
        channel::Message,
//        event::MessageUpdateEvent,
        gateway::Ready,
//        guild::{Member, Role},
        guild::Member,
//        id::{ChannelId, GuildId, MessageId, RoleId},
        id::{ChannelId, GuildId},
        user::User,
    },
    prelude::*,
};

/*
use std::env::args;
use tokio::prelude::*;
use serenity::model::channel::MessageAttachment;
use serenity::{
    async_trait,
    model::{
        channel::Message,
        gateway::Ready,
        guild::Member,
        id::{ChannelId, GuildId},
        user::User,
    },
    prelude::*,
};*/

struct Handler;

#[async_trait]
impl EventHandler for Handler {
    async fn message(&self, ctx: Context, msg: Message) {
        // Don't respond to messages from other bots.
        if msg.author.bot {
            return;
        }

        // Map from trigger words/phrases to responses.
        let triggers = [
            ("bitch", "LASAGNA!!!"),
            ("I'm", "Hi %, I'm dad."),
            ("uwu", "OwO"),
            ("oof", "no"),
            ("mallcop", "A mustache a day keeps the shoplifters at bay"),
            ("nooo", "https://tenor.com/view/no-theoffice-stevecarrell-michaelscott-gif-4652931"),
            ("bad bot", "you're not my dad"),
            ("peter", "feature coming soon"),
            (":(", "https://tenor.com/view/30rock-alec-baldwin-there-there-cheer-up-comfort-gif-4215371"),
        ];

        // Check if any of the trigger words/phrases appear in the message.
        let response = triggers
            .iter()
            .filter(|(trigger, _)| msg.content.to_lowercase().contains(trigger))
            .map(|(_, response)| response)
            .nth(0);


        // If a trigger word/phrase was found, send the corresponding response.
        if let Some(response) = response {
//            if response == "peter.mp4" {
                // If the response is "peter.mp4", send the file with that name.

//                let file = serenity::http::MessageAttachment::Path {
//                    file: "resources/peter.mp4",
//                    name: Some("peter.mp4"),
//                };
//                if let Err(why) = msg.channel_id.send_message(&ctx.http, |m| m.add_file(file)).await {
//                    println!("Error sending message: {:?}", why);
//                }
//            } else {
                // Otherwise, send the response as a regular message.
                if let Err(why) = msg.channel_id.say(&ctx.http, response).await {
                    println!("Error sending message: {:?}", why);
                }
//            }
            println!("{}", response);
        }
    }
    async fn guild_member_addition(&self, ctx: Context, _guild_id: GuildId, new_member: Member) {
        let channel_id = ChannelId::from(510553881764298766 as u64);
        if let Err(why) = channel_id.say(&ctx.http, ("hey look, its a ".to_owned() + &new_member.user.mention())).await {
            println!("Error sending message: {:?}", why);
        }
    }

    async fn guild_member_removal(&self, ctx: Context, _guild_id: GuildId, user: User) {
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
    let mut client = Client::builder(&token)
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
